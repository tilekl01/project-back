# from rest_framework import models
from django.shortcuts import render
from .models import News


def get_news(request):
    news = News.objects.all()
    return render (request, {'news': news})
    
# def news_detail(request, id):
#     news = Tour.objects.all(id=id)
#     return render (request, {'news': news})