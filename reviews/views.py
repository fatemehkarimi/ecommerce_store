from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import GeneralProduct
from .models import Review
# Create your views here.

class UserReviewCreateView(LoginRequiredMixin, View):
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        review_body = request.POST.get('review_text')
        review_rate = request.POST.get('review_rate', 0)
        product = GeneralProduct.objects.get(pk=kwargs['pk'])
        Review.objects.create(user=self.request.user, product=product,
            review_body=review_body, rate=review_rate)

        next = request.GET.get('next')
        if next:
            success_url = next
        else:
            success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)
        

class UserReviewDeleteView(LoginRequiredMixin, View):
    login_url = 'account_login'
    def post(self, request, *args, **kwargs):
        Review.objects.filter(pk=kwargs['pk']).delete()

        next = request.GET.get('next')
        if next:
            success_url = next
        else:
            success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)