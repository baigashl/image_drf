import io
from rest_framework import serializers
from rest_framework.reverse import reverse

from gallery.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        if request != {}:
            print(request.data['cover'].file)
            b = io.BytesIO(request.data['cover'].file)
            print(type(b))
            with open("test.xlsx") as f:  ## Excel File
                print(type(f))  ## Open file is TextIOWrapper
                bw = io.TextIOWrapper(b)  ## Conversion to TextIOWrapper
                print(type(bw))
        return reverse("detail", kwargs={'id': obj.id}, request=request)
