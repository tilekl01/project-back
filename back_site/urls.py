"""
URL configuration for back_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


api_urlpatterns = [
    path('', include('apps.discover.api.urls')),
    path('', include('apps.life_style.api.urls')),
    path('', include('apps.music_news.api.urls')),
    path('', include('apps.news.api.urls')),
    path('', include('apps.popular.api.urls')),
    path('', include('apps.popular_post.api.urls')),
    path('', include('apps.social_posts.api.urls')),

]
include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('discover/', include('apps.discover.urls')),
    path('life_style/', include('apps.life_style.urls')),
    path('music_news/', include('apps.music_news.urls')),
    path('news/', include('apps.news.urls')),
    path('popular/', include('apps.popular.urls')),
    path('popular_post/', include('apps.popular_post.urls')),
    path('social_posts', include('apps.social_posts.urls')),
    path('api/', include(api_urlpatterns)),
]


