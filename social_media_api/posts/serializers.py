from rest_framework import serializers
from .models import Post, Comment, Like

#Generic de commentaire
class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "created_at")

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "user", "content", "image", "created_at", "comments")




#generic de 'j'aime' d'un post 
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "post", "user")
        read_only_fields = ("user",)
