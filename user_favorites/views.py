from django.shortcuts import render
from django.views.generic import View, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import UserFavorites
from products.models import GeneralProduct

# Create your views here.
class UserFavoritesListView(LoginRequiredMixin, ListView):
    model = UserFavorites
    template_name = 'account/user_favorites.html'
    context_object_name = 'favorites'
    login_url = 'account_login'

    def get_queryset(self, **kwargs):
        return UserFavorites.objects.filter(user=self.request.user)


class FavDeleteView(LoginRequiredMixin, DeleteView):
    model = UserFavorites
    login_url = 'account_login'

    def get_success_url(self, **kwargs):
        next = self.request.GET.get('next')
        if next:
            success_url = next
        else:
            success_url = reverse_lazy('user_favorites')
        return success_url

class FavCreateView(LoginRequiredMixin, View):
    login_url = 'account_login'

    def post(self, request, *args, **kwargs):
        user = self.request.user
        product = GeneralProduct.objects.get(pk=self.kwargs['pk'])
        fav = UserFavorites.objects.filter(user=user, product=product)
        if not fav:
            UserFavorites.objects.create(user=user, product=product)

        next = self.request.GET.get('next')
        if next:
            success_url = next
        else:
            success_url = reverse_lazy('user_favorites')
        return HttpResponseRedirect(success_url)
