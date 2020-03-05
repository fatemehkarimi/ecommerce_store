from django.urls import path

from .views import (
    ProductBySubCategoryListView,
    ProductDetailView,
    ProductSearchResultListView,
)

urlpatterns = [
    path('by/subcategory/',
        ProductBySubCategoryListView.as_view(), name='product_subcat'),
    path('search/result',
        ProductSearchResultListView.as_view(), name='product_search_result'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
