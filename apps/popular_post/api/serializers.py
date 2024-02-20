from rest_framework.serializers import ModelSerializer

from apps.popular_post.models import Popular_post


class PopularpostSerializer(ModelSerializer):
    class Meta:
        model = Popular_post
        fields = [
            "id",
            "category",
            "image",
            "title",
            "created_at",
        ]