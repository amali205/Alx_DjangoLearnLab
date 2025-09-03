from django.shortcuts import render
from rest_framework import viewsets , filters , permissions
from .models import Post, Comment   
from .serializers import PostSerializer, CommentSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'tiltle', 'content']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Replace the following line with your actual logic to get following users
        following_users = user.following.all() if hasattr(user, 'following') else []
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'content', 'post__id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


