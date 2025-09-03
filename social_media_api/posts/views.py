from django.shortcuts import render
from rest_framework import viewsets , filters
from .models import Post, Comment   
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics , permissions

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'tiltle', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   



class FollowingPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get all users the current user is following
        following_users = self.request.user.following.all()
        # filter posts by those authors and order by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'content', 'post__id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if post.likes.filter(user=user).exists():
            # User has already liked this post, so unlike it
            post.likes.filter(user=user).delete()
            return Response({'status': 'unliked'})
        else:
            # Like the post
            post.likes.create(user=user)
            return Response({'status': 'liked'})
        

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if post.likes.filter(user=user).exists():
            # User has already liked this post, so unlike it
            post.likes.filter(user=user).delete()
            return Response({'status': 'unliked'})
        else:
            return Response({'status': 'not liked yet'}, status=400)        