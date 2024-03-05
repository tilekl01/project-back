from rest_framework.serializers import ModelSerializer

from apps.popular.models import Popular


class PopularSerializer(ModelSerializer):
    class Meta:
        model = Popular
        fields = [
            "id",
            "category",
            "image",
            "title",
            "created_at",
            "comment",
            "is_active",
        ]