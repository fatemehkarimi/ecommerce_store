from django.urls import path

from .views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
]
