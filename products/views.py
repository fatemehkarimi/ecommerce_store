from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.views.generic import ListView, DetailView, DeleteView

from user_favorites.models import UserFavorites
from reviews.models import Review
from reviews.rate_analyze import RateAnalyze

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
            context['countable_product_info'] = CountableProduct.objects.filter(
                product=self.object).first()
        else:
            context['uncountable_product_info'] = UnCountableProduct.objects.filter(
                product=self.object).first()

        #check if product is in favorite list or not
        
        if self.request.user.is_authenticated:
            fav = UserFavorites.objects.filter(user=self.request.user, product=self.object).first()
            context['item_is_faved'] = fav if fav else None

        context['reviews'] = Review.objects.filter(product=self.object)

        rate_analyze = RateAnalyze(product=self.object)
        context['avg_product_rate'] = rate_analyze.get_avg_rating()
        context['rate_diagram'] = rate_analyze.get_rate_plot()
        return context


class ProductSearchResultListView(ListView):
    model = GeneralProduct
    context_object_name = 'matched_products'
    template_name = 'products/product_search_result.html'

    def get_queryset(self):
        name = self.request.GET.get('product_name')
        return GeneralProduct.objects.filter(
            Q(product_name__icontains=name)
            | Q(subcategory__subcategory_name__icontains=name))

