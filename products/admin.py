from django.contrib import admin
from .models import Category, SubCategory, Brand, GeneralProduct

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['parent_category', 'subcategory_name',]

class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'brand_website',]

class GenralProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'subcategory', 'price',]

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(GeneralProduct, GenralProductAdmin)