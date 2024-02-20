from rest_framework.serializers import ModelSerializer

from apps.discover.models import Discover


class DiscoverSerializer(ModelSerializer):
    class Meta:
        model = Discover
        fields = [
            "id",
            "image",
            "title",
        ]