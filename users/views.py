from django.shortcuts import render
from django.views import View

from .models import UserProfile

# Create your views here.


class UserProfileView(View):
    template_name = 'account/user_profile.html'


    def get(self, request, *args, **kwargs):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context = {
            'profile': profile,
            'user': self.request.user
        }
        return render(request, self.template_name, context)
    