from rest_framework.viewsets import ModelViewSet

from apps.life_style.models import Life_Style
from apps.life_style.api.serializers import Life_StyleSerializer


class Life_StyleApiViewSet(ModelViewSet):
    queryset = Life_Style.objects.all()
    serializer_class = Life_StyleSerializer