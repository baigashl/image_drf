from rest_framework import serializers
from rest_framework.reverse import reverse

from gallery.models import Post


class PostSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'image']

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     return reverse("detail", kwargs={'id': obj.id}, request=request)
