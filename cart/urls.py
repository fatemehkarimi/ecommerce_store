from django.urls import path

from .views import CartListView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='view_cart'),
]
