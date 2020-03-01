from django import forms
from collections import OrderedDict
from django.contrib.auth import get_user_model

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()