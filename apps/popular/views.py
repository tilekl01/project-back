from django.shortcuts import render
from .models import Popular

def get_popular(request):
    popular = Popular.objects.all()
    return render (request, {'popular': popular})


# def index(request):
#     popular = Popular.objects.all()
#     return render (request, {'popular': popular})

# def popular_detail(request, id):
#     popular = Popular.objects.get(id=id)
#     return render (request, {'popular': popular})