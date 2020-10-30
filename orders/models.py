from django.contrib.auth import get_user_model
from django.db import models

from users.models import UserAddress
from products.models import GeneralProduct

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = [
        (1, 'In queue'),
        (2, 'Approved'),
        (3, 'Preparing your order'),
        (4, 'Delivering to customer'),
        (5, 'Delivered')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    net_sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    destination_address = models.ForeignKey(
        UserAddress, on_delete=models.SET_NULL, null=True, blank=True)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=1)

    def __str__(self):
        return str(self.pk)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(GeneralProduct, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.count
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)
