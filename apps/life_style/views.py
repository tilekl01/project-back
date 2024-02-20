from django.shortcuts import render
from .models import Life_Style

def get_life_style(request):
    life_style = Life_Style.objects.all()
    return render (request, {'life_style': life_style})