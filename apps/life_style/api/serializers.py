from rest_framework.serializers import ModelSerializer

from apps.life_style.models import Life_Style


class Life_StyleSerializer(ModelSerializer):
    class Meta:
        model = Life_Style
        fields = [
            "id",
            "category",
            "image",
            "title",
            "created_at",
        ]