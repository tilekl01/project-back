from rest_framework.routers import DefaultRouter

from apps.news.api.views import NewsApiViewSet

router = DefaultRouter()
router.register(
    r'news',
    NewsApiViewSet
)

urlpatterns = router.urls