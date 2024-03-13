from rest_framework.routers import DefaultRouter

from apps.categories.api.views import CategoryApiViewSet

router = DefaultRouter()
router.register(
    r'categories',
    CategoryApiViewSet
)

urlpatterns = router.urls