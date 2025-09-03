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




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Post, Like


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        # Prevent duplicate likes
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, post=post)

        # TODO: Generate notification here if you have notifications model
        return Response({"message": f"You liked '{post.title}'"}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"message": f"You unliked '{post.title}'"}, status=status.HTTP_200_OK)
