from rest_framework.viewsets import ModelViewSet

from apps.social_posts.models import Social_Posts
from apps.social_posts.api.serializers import Social_postsSerializer


class Social_PostsApiViewSet(ModelViewSet):
    queryset = Social_Posts.objects.all()
    serializer_class = Social_postsSerializer