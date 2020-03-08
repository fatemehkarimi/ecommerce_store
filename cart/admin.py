from django.contrib import admin

from .models import Cart, CartItem
# Register your models here.

class CartItemsInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemsInline
    ]

    list_display = ('cart_str', 'creation_date', 'expiration_date', )

    def cart_str(self, obj):
        return obj.__str__()

admin.site.register(Cart, CartAdmin)