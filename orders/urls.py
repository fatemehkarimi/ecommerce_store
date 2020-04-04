from django.urls import path
from django.conf.urls import url
from .views import SubmitOrderView, send_request, verify

urlpatterns = [
    path('submit/order/', SubmitOrderView.as_view(), name='submit_order'),
    url('request/', send_request, name='request'),
    url('verify/', verify, name='verify'),
]
