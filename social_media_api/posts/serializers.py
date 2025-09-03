from .models import Post, comment
from rest_framework import serializers  



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'tiltle', 'content', 'created_at', 'updated_at']  



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = comment
        fields = ['id', 'post', 'user', 'content', 'created_at', 'updated_at']      




        
                