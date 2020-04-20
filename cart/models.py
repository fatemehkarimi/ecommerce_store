from django.db import models
from datetime import datetime, timedelta

# Create your models here.
from products.models import GeneralProduct
from users.models import UserAddress

class Cart(models.Model):
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)
    destination_address = models.ForeignKey(
        UserAddress, blank=True, null=True,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return str(self.pk)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(GeneralProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('cart', )

    def __str__(self):
        return self.product.product_name
    