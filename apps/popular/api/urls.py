from rest_framework.routers import DefaultRouter

from apps.popular.api.views import PopularApiViewSet

router = DefaultRouter()
router.register(
    r'popular',
    PopularApiViewSet
)

urlpatterns = router.urls