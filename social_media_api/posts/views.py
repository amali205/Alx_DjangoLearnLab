from django.shortcuts import render
from rest_framework import viewsets , filters
from .models import Post, comment   
from .serializers import PostSerializer, CommentSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'tiltle', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   


class CommentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'content', 'post__id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


