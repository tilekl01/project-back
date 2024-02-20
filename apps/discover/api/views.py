from rest_framework.viewsets import ModelViewSet

from apps.discover.models import  Discover
from apps.discover.api.serializers import DiscoverSerializer


class DiscoverApiViewSet(ModelViewSet):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer