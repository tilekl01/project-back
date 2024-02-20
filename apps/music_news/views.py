from django.shortcuts import render
from .models import Music_News


def get_music_news(request):
    music_news = Music_News.objects.all()
    return render (request, {'music_news': music_news})