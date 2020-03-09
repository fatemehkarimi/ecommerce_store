from django.views.generic import View, ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse

from .models import Cart, CartItem
from .cart import _Cart

# Create your views here.

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