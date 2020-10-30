from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order, OrderItem

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
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        order_id = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        itms = OrderItem.objects.filter(order=order_id)
        context["items"] = itms
        return context
    