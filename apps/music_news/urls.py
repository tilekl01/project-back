from django.urls import path
from .views import get_music_news

urlpatterns = [
    path('', get_music_news, name='get_music_news'),
]