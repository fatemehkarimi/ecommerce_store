from django.urls import path

from .views import CartListView, AddItemToCartView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='view_cart'),
    path('add/item/<int:pk>/',
        AddItemToCartView.as_view(), name='add_item_to_cart'),
]
