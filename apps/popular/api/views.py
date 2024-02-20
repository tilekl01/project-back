from rest_framework.viewsets import ModelViewSet

from apps.popular.models import Popular
from apps.popular.api.serializers import PopularSerializer


class PopularApiViewSet(ModelViewSet):
    queryset = Popular.objects.all()
    serializer_class = PopularSerializer