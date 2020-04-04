from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemAdmin
    ]

    list_display = ['pk', 'order_date', 'total_paid', 'order_status']

admin.site.register(Order, OrderAdmin)