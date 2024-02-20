from django.shortcuts import render
from.models import Popular_post

def get_popular_post(request):
    popular = Popular_post.objects.all()
    return render (request, {'popular': popular})