from rest_framework.serializers import Serializer
from apps.users.models import User


class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "age",
            "job",
            "gender",
            "phone_number",
            "instagram",
        ]