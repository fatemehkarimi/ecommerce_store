from django.urls import path

from .views import(
    UserFavoritesListView,
    FavDeleteView,
    FavCreateView,
)

urlpatterns = [
    path('delete/fav/<int:pk>/', FavDeleteView.as_view(), name='delete_fav'),
    path('add/fav/<int:pk>/', FavCreateView.as_view(), name='create_fav'),
    path('', UserFavoritesListView.as_view(), name='user_favorites'),
]
