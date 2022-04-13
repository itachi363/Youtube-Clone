from rest_framework import serializers
from models import Comment

class CommentSerializer(serializers.ModelField):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']