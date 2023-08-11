from rest_framework import serializers
from .models import Post
from apps.review.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'        
        # fields = ['body']   
        # exclude = ['author'] 

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['author'] = instance.author.username
        return rep
