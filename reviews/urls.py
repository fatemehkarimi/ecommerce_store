from django.urls import path

from .views import UserReviewCreateView, UserReviewDeleteView

urlpatterns = [
    path('add/new/<int:pk>/', UserReviewCreateView.as_view(), name='write_review'),
    path('delete/<int:pk>/', UserReviewDeleteView.as_view(), name='delete_review'),
]
