from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from .models import UserProfile, UserAddress
from .forms import EditProfileForm
# Create your views here.

class UserProfileView(LoginRequiredMixin, View):
    template_name = 'account/user_profile.html'
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context = {
            'profile': profile,
            'user': self.request.user
        }
        return render(request, self.template_name, context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    login_url = 'account_login'


class AddNewAddressView(LoginRequiredMixin, CreateView):
    model = UserAddress
    fields = ('city', 'adress', 'zip_code',)
    template_name = 'account/add_new_address.html'
    login_url = 'account_login'

    def get_success_url(self):
        return reverse_lazy('user_addresses')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressListView(LoginRequiredMixin, ListView):
    model = UserAddress
    template_name = 'account/user_addresses.html'
    context_object_name = 'addresses'
    login_url = 'account_login'

    def get_queryset(self, **kwargs):
        return UserAddress.objects.filter(user=self.request.user)


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = UserAddress
    success_url = reverse_lazy('user_addresses')
    login_url = 'account_login'

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAddress
    fields = ('city', 'adress', 'zip_code',)
    success_url = reverse_lazy('user_addresses')
    template_name = 'account/update_address.html'
    login_url = 'account_login'

