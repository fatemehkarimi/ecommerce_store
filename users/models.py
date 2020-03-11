from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from .validators import PHONE_REGEX, profile_pic_size_limit

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
        editable=False
    )
    profile_img = models.ImageField(
        upload_to="profile_pics",
        blank=True,
        null=True,
        validators=[profile_pic_size_limit]
    )
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(
        validators=[PHONE_REGEX],
        max_length=17, blank=True, null=True
    )

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("user_profile")

class UserAddress(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    adress = models.TextField()
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.zip_code
    