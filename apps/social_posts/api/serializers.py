from rest_framework.serializers import ModelSerializer

from apps.social_posts.models import Social_Posts


class Social_postsSerializer(ModelSerializer):
    class Meta:
        model = Social_Posts
        fields = [
            "id",
            "image",
            "title",
            "created_at",
        ]