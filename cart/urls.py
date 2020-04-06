from django.urls import path

from .views import (
    CartListView,
    AddItemToCartView,
    RemoveItemFromCart,
    ShippingAddresses,
    charge
)

urlpatterns = [
    path('cart/', CartListView.as_view(), name='view_cart'),
    path('shipping/info/', ShippingAddresses.as_view(), name='shipping_info'),
    path('add/item/<int:pk>/',
        AddItemToCartView.as_view(), name='add_item_to_cart'),
    path('remove/item/<int:pk>/',
        RemoveItemFromCart.as_view(), name='remove_item_from_cart'),
    path('charge/', charge, name='charge'),    
]
