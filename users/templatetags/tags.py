from django import template
from users.models import UserProfile

register =template.Library()

@register.simple_tag
def get_user_profile(request):
    return UserProfile.objects.get(user=request.user).profile_img.url