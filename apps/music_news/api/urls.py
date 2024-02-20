from rest_framework.routers import DefaultRouter

from apps.music_news.api.views import Music_NewsApiViewSet

router = DefaultRouter()
router.register(
    r'music_news',
    Music_NewsApiViewSet
)

urlpatterns = router.urls