from django.shortcuts import render
from django.views.generic import ListView

from .models import GeneralProduct

# Create your views here.
class ProductBySubCategoryListView(ListView):
    model = GeneralProduct
    context_object_name = 'products_by_subcat'
    template_name = 'products/product_by_subcategory.html'

    def get_queryset(self):
        subcat = self.request.GET.get('subcat')
        return GeneralProduct.objects.filter(subcategory__subcategory_name=subcat)