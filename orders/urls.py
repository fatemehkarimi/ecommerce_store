from django.urls import path

from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('details/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('', OrderListView.as_view(), name='orders'),
]
