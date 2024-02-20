from django.urls import path
from .views import get_popular

urlpatterns = [
    path('popular/', get_popular, name='get_popular'),
]