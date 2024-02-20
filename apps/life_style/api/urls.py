from rest_framework.routers import DefaultRouter

from apps.life_style.api.views import Life_StyleApiViewSet

router = DefaultRouter()
router.register(
    r'life_style',
    Life_StyleApiViewSet
)

urlpatterns = router.urls