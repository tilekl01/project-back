from rest_framework.serializers import ModelSerializer

from apps.news.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            "id",
            "category",
            "image",
            "title",
            "by_name",
            "created_at",
        ]