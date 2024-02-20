from rest_framework.viewsets import ModelViewSet

from apps.news.models import News
from apps.news.api.serializers import NewsSerializer


class NewsApiViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer