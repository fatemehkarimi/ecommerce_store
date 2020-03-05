from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import (
    GeneralProduct,
    UnCountableProduct,
    CountableProduct
)

# Create your views here.
class ProductBySubCategoryListView(ListView):
    model = GeneralProduct
    context_object_name = 'products_by_subcat'
    template_name = 'products/product_by_subcategory.html'

    def get_queryset(self):
        subcat = self.request.GET.get('subcat')
        return GeneralProduct.objects.filter(
            subcategory__subcategory_name=subcat
        )


class ProductDetailView(DetailView):
    model = GeneralProduct
    template_name = 'products/product_detail.html'
    cotext_object_name = 'general_product_info'
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if self.object.is_countable:
            context['countable_product_info'] = CountableProduct.objects.get(
                pk=self.object.pk)
        else:
            context['uncountable_product_info'] = UnCountableProduct.objects.get(
                pk=self.object.pk)
        return context


class ProductSearchResultListView(ListView):
    model = GeneralProduct
    context_object_name = 'matched_products'
    template_name = 'products/product_search_result.html'

    def get_queryset(self):
        name = self.request.GET.get('product_name')
        return GeneralProduct.objects.filter(
            Q(product_name__icontains=name)
            | Q(subcategory__subcategory_name__icontains=name)
            | Q(subcategory__parent_category__category_name__icontains=name))

    