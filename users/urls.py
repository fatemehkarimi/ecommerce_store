from django.urls import path
from .views import UserProfileView, EditProfileView

urlpatterns = [
    path('user/profile/<int:pk>/',
        UserProfileView.as_view(), name="user_profile"),
    path('user/profile/edit/<int:pk>/',
        EditProfileView.as_view(), name="profile_edit"),
]
