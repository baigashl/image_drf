from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from gallery.api.serializers import PostSerializer
from gallery.models import Post
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)


class PostListAPIView(ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
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
        serializer.save()
        images = self.request.FILES
        serializer.save(image=images['image'])


class PostCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny,]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        images = self.request.FILES
        serializer.save(image=images['image'])

class PostDetailAPIView(RetrieveAPIView):
    print('qweqwe')
    permission_classes = [AllowAny,]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer

