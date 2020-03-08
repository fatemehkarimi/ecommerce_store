from django.views.generic import ListView
from django.shortcuts import render

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