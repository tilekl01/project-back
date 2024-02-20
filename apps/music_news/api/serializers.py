from rest_framework.serializers import ModelSerializer

from apps.music_news.models import Music_News


class Music_NewsSerializer(ModelSerializer):
    class Meta:
        model = Music_News
        fields = [
            "id",
            "category",
            "image",
            "title",
            "created_at",
            "text",
            "comment",
        ]