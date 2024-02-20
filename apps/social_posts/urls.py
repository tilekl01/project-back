from django.urls import path
from .views import get_social_posts

urlpatterns = [
    path('', get_social_posts, name='get_social_posts'),
]