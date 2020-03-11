from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import UserProfile, UserAddress

# Register your models here.
user = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = user
    list_display = ['email', 'username',]

admin.site.register(user, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(UserAddress)
