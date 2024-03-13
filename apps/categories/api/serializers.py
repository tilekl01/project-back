from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
        ]