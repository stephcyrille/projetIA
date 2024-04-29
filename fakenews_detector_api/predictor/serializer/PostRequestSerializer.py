from rest_framework import serializers
from predictor.models import PostRequest

class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRequest
        exclude = ['id']