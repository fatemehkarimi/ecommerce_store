from django.db import models
from django.contrib.auth import get_user_model

from products.models import GeneralProduct

# Create your models here.
class UserFavorites(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(GeneralProduct, on_delete=models.CASCADE)
