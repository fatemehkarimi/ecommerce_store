from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from products.models import GeneralProduct

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(GeneralProduct, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    review_body = models.TextField()
    review_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.review_date = timezone.now()
        return super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.review_body[:50]
    