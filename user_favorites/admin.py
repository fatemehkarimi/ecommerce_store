from django.contrib import admin

from .models import UserFavorites
# Register your models here.

class UserFavoritesAdmin(admin.ModelAdmin):
    model = UserFavorites

admin.site.register(UserFavorites, UserFavoritesAdmin)