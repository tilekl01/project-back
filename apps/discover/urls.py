from django.urls import path
from .views import get_discover

urlpatterns = [
    path('', get_discover, name='get_discover'),
]