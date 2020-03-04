from django.urls import path

from .views import ProductBySubCategoryListView

urlpatterns = [
    path('by/subcategory/',
        ProductBySubCategoryListView.as_view(), name='product_subcat'),
]
