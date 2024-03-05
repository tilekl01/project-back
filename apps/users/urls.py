from rest_framework.routers import DefaultRouter
from apps.users.views import UsertViewSet

router = DefaultRouter()

router.register(
    r'users',
    UsertViewSet
)

urlpatterns = router.urls
