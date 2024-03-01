
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


api_urlpatterns = [
    path('', include('apps.discover.api.urls')),
    path('', include('apps.life_style.api.urls')),
    path('', include('apps.music_news.api.urls')),
    path('', include('apps.news.api.urls')),
    path('', include('apps.popular.api.urls')),
    path('', include('apps.popular_post.api.urls')),
    path('', include('apps.social_posts.api.urls')),
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

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


