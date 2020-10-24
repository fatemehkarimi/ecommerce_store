from django.views.generic import View, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings

import stripe

from .models import Cart, CartItem
from users.views import AddressListView
from .cart import _Cart
from orders.models import Order, OrderItem

# Create your views here.
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
class CartListView(ListView):
    model = CartItem
    template_name = 'orders/view_cart.html'
    context_object_name = 'items'

    def dispatch(self, request, *args, **kwargs):
        self.cart = _Cart(request)
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.cart.get_items_list()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_total'] = self.cart.sum_total()
        return context


class AddItemToCartView(View):

    def dispatch(self, request, *args, **kwargs):
        self.cart = _Cart(request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        quantity = request.POST.get('quantity', 1)
        self.cart.add_item_to_cart(product_pk=kwargs['pk'], quantity=quantity)
        return HttpResponseRedirect(reverse('view_cart'))


class RemoveItemFromCart(View):

    def dispatch(self, request, *args, **kwargs):
        self.cart = _Cart(request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.cart.remove_item_from_cart(kwargs['pk'])
        return HttpResponseRedirect(reverse('view_cart'))

class ShippingAddresses(AddressListView):
    template_name = 'orders/shipping_info.html'

    def dispatch(self, request, *args, **kwargs):
        self.cart = _Cart(request)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_total'] = self.cart.sum_total()
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY

        ship_address_id = self.request.GET.get('selected_address')
        if ship_address_id:
            ship_address_id = int(ship_address_id)
            self.cart.set_ship_address(ship_address_id)
            context['ship_address'] = self.cart.get_ship_address()
            context['ship_cost'] = self.cart.ship_cost.get_city_cost(self.cart.cart.destination_address.city)
            context['must_pay'] = self.cart.shopping_shipping_total_cost()
            context['stripe_amount'] = self.cart.get_stripe_cost()
        return context


def charge(request):
    if request.method == 'POST':
        cart = _Cart(request)
        #TODO: handle if no destination address is set.

        charge = stripe.Charge.create(
            amount=cart.get_stripe_cost(),
            currency='usd',
            source=request.POST['stripeToken']
        )

        new_order = submitOrder(request, cart)
        add_order_items(new_order, cart)
        cart.delete_cart()
        return render(request, 'orders/success_purchase.html')


def submitOrder(request, cart):
    new_order = Order.objects.create(
        user=request.user,
        net_sale_amount=cart.sum_total(),
        shipping_amount=cart.get_shipping_cost(),
        total_paid=cart.shopping_shipping_total_cost(),
        destination_address=cart.get_ship_address()
    )
    return new_order

def add_order_items(order, cart):
    items = cart.get_items_list()
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            count=item.quantity,
            unit_price=item.product.price_per_unit
        )
    return