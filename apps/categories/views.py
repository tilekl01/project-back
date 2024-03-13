from django.shortcuts import render
from. models import Category

def get_category(request):
    category = Category.objects.all()
    return render (request, {'category': category})