from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/user_orders.html'
    context_object_name = 'orders'
    login_url = 'account_login'

    def get_queryset(self, **kwargs):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_details.html'
    context_object_name = 'order'