import io
from rest_framework import serializers
from rest_framework.reverse import reverse

from gallery.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'url']

    # def create(self, validated_data):
    #     images = self.context['request'].FILES
    #     m1 = Post.objects.create(
    #         **validated_data
    #     )
    #     # print(type(images['cover']))
    #     # with open(images['cover'], 'rb') as f:
    #     #     print(f.read())
    #
    #     # m1.image.add(images['cover'])
    #     return m1

    def get_url(self, obj):
        request = self.context.get('request')
        # if request.data != {}:
        #     print(request.data)
        #     print(type(request.FILES['cover']))
        return reverse("detail", kwargs={'id': obj.id}, request=request)
