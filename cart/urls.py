from django.urls import path

from .views import CartListView, AddItemToCartView, RemoveItemFromCart

urlpatterns = [
    path('cart/', CartListView.as_view(), name='view_cart'),
    path('add/item/<int:pk>/',
        AddItemToCartView.as_view(), name='add_item_to_cart'),
    path('remove/item/<int:pk>/',
        RemoveItemFromCart.as_view(), name='remove_item_from_cart'),
]
