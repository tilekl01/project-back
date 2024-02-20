from django.urls import path
from .views import get_popular_post

urlpatterns = [
    path('popular_post/', get_popular_post, name='get_popular_post'),
]