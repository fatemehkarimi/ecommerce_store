from django.db import models
from datetime import datetime, timedelta
from products.models import GeneralProduct

# Create your models here.

class Cart(models.Model):
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)

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
    