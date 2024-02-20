from rest_framework.viewsets import ModelViewSet

from apps.popular_post.models import Popular_post
from apps.popular_post.api.serializers import PopularpostSerializer


class Popular_postApiViewSet(ModelViewSet):
    queryset = Popular_post.objects.all()
    serializer_class = PopularpostSerializer