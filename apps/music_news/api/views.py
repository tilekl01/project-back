from rest_framework.viewsets import ModelViewSet

from apps.music_news.models import Music_News
from apps.music_news.api.serializers import Music_NewsSerializer


class Music_NewsApiViewSet(ModelViewSet):
    queryset = Music_News.objects.all()
    serializer_class = Music_NewsSerializer