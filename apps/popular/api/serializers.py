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
            "by_name",
            "created_at",
        ]