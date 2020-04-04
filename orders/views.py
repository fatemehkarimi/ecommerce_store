from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect

#third party
from zeep import Client

#local
from .models import Order, OrderItem
from users.models import UserAddress
from cart.models import Cart, CartItem
from cart.cart import _Cart

MERCHANT = '12345678-1234-1234-1234-123456789000'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "finalize your order"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/orders/verify/' # Important: need to edit for realy server.

def send_request(request):
    result = client.service.PaymentRequest(
        MERCHANT, amount, description, email, mobile, CallbackURL)

    if result.Status == 100:
        return redirect(
            'https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error Code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success\nRefId: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted: ' + str(result.Status))
        else:
            return HttpResponse('Transaction Failed.\nStatus: ', str(result.Status))
    else:
        return HttpResponse('Transaction Failed or canceled by user')

class SubmitOrderView(View):

    def post(self, request, *args, **kwargs):
        customer = self.request.user
        shopped_cart = _Cart(request)
        net_sale_amount = shopped_cart.sum_total()
        shipping_amount = self.POST.get('shipping_cost')
        total_paid = net_sale_amount + shipping_amount
        address_id = self.POST.get('destin_address')
        destin_address = UserAddress.objects.filter(pk=address_id)

        submited_order = Order.objects.create(
            user=customer,
            net_sale_amount=net_sale_amount,
            shipping_amount=shipping_amount,
            total_paid=total_paid, 
            destination_address=destin_address
        )

        cart_items = shopped_cart.get_items_list()
        for item in cart_items:
            OrderItem.objects.create(
                order_id=submited_order,
                item=item.product,
                count=item.quantity,
                unit_price=item.product.price_per_unit
            )
        return render(request, 'orders/success_order.html')
