from django.shortcuts import render
from django.views import View
from django.views.generic.edit import UpdateView

from .models import UserProfile
from .forms import EditProfileForm
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
    
class EditProfileView(UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'