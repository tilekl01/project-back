from django.urls import path
from .views import get_life_style

urlpatterns = [
    path('life_style/', get_life_style, name='get_life_style'),
]