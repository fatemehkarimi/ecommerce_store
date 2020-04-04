from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import F, Sum, DecimalField
from .models import Cart, CartItem

CART_ID = 'CART-ID'

class _Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            cart = Cart.objects.filter(id=cart_id, checked_out=False).first()
            if cart is None:
                cart = self.new_cart(request)
        else:
            cart = self.new_cart(request)
        self.cart = cart

    def new_cart(self, request):
        cart = Cart.objects.create(
            creation_date=datetime.now(),
            expiration_date=datetime.now() + timedelta(days=20)
        )
        request.session[CART_ID] = cart.id
        return cart

    def delete_cart(self, cart):
        cart.delete()

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

    def sum_total(self):
        item_set = self.get_items_list()
        return item_set.aggregate(
            total=Sum(F('quantity') * F('product__price_per_unit'),
            output_field=DecimalField(
                max_digits=10, decimal_places=0)
        )).get('total', 0)