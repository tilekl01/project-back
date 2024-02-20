from rest_framework.routers import DefaultRouter

from apps.popular_post.api.views import Popular_postApiViewSet

router = DefaultRouter()
router.register(
    r'popular',
    Popular_postApiViewSet
)

urlpatterns = router.urls