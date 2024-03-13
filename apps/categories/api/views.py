from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from apps.categories.api.serializers import CategoriesSerializer


class Life_StyleApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer