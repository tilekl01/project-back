from django.urls import path
from .views import get_category

urlpatterns = [
    path('', get_category, name='get_category'),
]