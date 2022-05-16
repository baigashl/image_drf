from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from rest_framework import permissions
from gallery.api.serializers import PostSerializer
from gallery.models import Post
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)


class PostListAPIView(ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

