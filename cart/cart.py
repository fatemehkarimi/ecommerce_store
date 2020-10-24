from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import F, Sum, DecimalField
from .models import Cart, CartItem

from .shipping_costs import ShippingCost
from users.models import UserAddress

CART_ID = 'CART-ID'

class _Cart:
    def __init__(self, request, address_id=None):
        cart_id = request.session.get(CART_ID)
        self.request = request
        if cart_id:
            cart = Cart.objects.filter(id=cart_id, checked_out=False).first()
            if cart is None:
                cart = self.new_cart()
        else:
            cart = self.new_cart()
        self.cart = cart
        if address_id:
            self.set_ship_address(address_id)
        self.ship_cost = ShippingCost()

    def new_cart(self):
        cart = Cart.objects.create(
            creation_date=datetime.now(),
            expiration_date=datetime.now() + timedelta(days=20)
        )
        self.request.session[CART_ID] = cart.id
        return cart

    def delete_cart(self):
        self.cart.delete()
        self.request.session.pop(CART_ID, None)

    def set_ship_address(self, address_id):
        self.cart.destination_address = UserAddress.objects.get(pk=address_id)
        self.cart.save()

    def get_ship_address(self):
        return self.cart.destination_address

    def get_items_list(self):
        return CartItem.objects.filter(cart=self.cart)

    def add_item_to_cart(self, product_pk, quantity=1):
        item_set = self.get_items_list()
        item = item_set.filter(product__pk=product_pk).first()

        if item:
            item.quantity = int(quantity)
            item.save()
        else:
            CartItem.objects.create(cart=self.cart, product_id=product_pk, quantity=int(quantity))

    def remove_item_from_cart(self, product_pk):
        item_set = self.get_items_list()
        item = item_set.filter(product__pk=product_pk).first()

        if item:
            item.delete()

    # get shopping cost
    def sum_total(self):
        item_set = self.get_items_list()
        return item_set.aggregate(
            total=Sum(F('quantity') * F('product__price_per_unit'),
            output_field=DecimalField(
                max_digits=10, decimal_places=0)
        )).get('total', 0)

    # get shipping cost
    def get_shipping_cost(self):
        return self.ship_cost.get_city_cost(
            self.cart.destination_address.city)

    # get shopping + shipping costs
    def shopping_shipping_total_cost(self):
        shopping_cost = self.sum_total()
        shipping_cost = self.ship_cost.get_city_cost(
            self.cart.destination_address.city)
        return shopping_cost + shipping_cost

    # get total costs in formatted for stipe
    def get_stripe_cost(self):
        return int(self.shopping_shipping_total_cost() * 100)