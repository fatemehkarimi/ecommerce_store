from django.urls import path
from .views import (
    UserProfileView,
    EditProfileView,
    AddNewAddressView,
    AddressListView,
    AddressDeleteView,
)

urlpatterns = [
    path('user/profile/<int:pk>/',
        UserProfileView.as_view(), name="user_profile"),
    path('user/profile/edit/<int:pk>/',
        EditProfileView.as_view(), name="profile_edit"),
    path('user/new/address/',
        AddNewAddressView.as_view(), name="add_new_address"),
    path('user/addresses/',
        AddressListView.as_view(), name='user_addresses'),
    path('user/delete/address/<int:pk>/',
        AddressDeleteView.as_view(), name='delete_address'),
]
