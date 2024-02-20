from rest_framework.routers import DefaultRouter

from apps.discover.api.views import DiscoverApiViewSet

router = DefaultRouter()
router.register(
    r'discover',
    DiscoverApiViewSet
)

urlpatterns = router.urls