from django.contrib import admin
from .models import (
    Category, SubCategory, Brand,
    GeneralProduct, CountableProduct, UnCountableProduct
)

class UnCountableProductInline(admin.TabularInline):
    model = UnCountableProduct

class CountableProductInline(admin.TabularInline):
    model = CountableProduct

class SubCategoryInline(admin.TabularInline):
    model = SubCategory

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SubCategoryInline
    ]

    list_display = ['category_name']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'brand_website',]

class GenralProductAdmin(admin.ModelAdmin):
    inlines = [
        UnCountableProductInline,
        CountableProductInline
    ]

    list_display = ['product_name', 'brand', 'subcategory',
        'price_per_unit', 'total_available_in_stock']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(GeneralProduct, GenralProductAdmin)