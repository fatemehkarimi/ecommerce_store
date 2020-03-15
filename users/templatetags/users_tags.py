from django import template

from users.models import UserProfile

register =template.Library()

@register.simple_tag
def get_user_profile(request):
    try:
        return UserProfile.objects.get(user=request.user).profile_img.url
    except:
        return '/static/images/NoProfilePic.png'

@register.simple_tag
def get_blank_stars(full_stars):
    return 5 - full_stars