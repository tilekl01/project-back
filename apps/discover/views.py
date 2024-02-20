from django.shortcuts import render
from .models import Discover


def get_discover(request):
    discovery = Discover.objects.all()
    return render (request, {'discovery': discovery})