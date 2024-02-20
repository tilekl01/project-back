from django.shortcuts import render
from. models import Social_Posts


def get_social_posts(request):
    social_posts = Social_Posts.objects.all()
    return render (request, {'social_posts': social_posts})