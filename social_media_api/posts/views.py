from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model  
from rest_framework import status, permissions, generics
from rest_framework.response import Response    
from django.shortcuts import get_object_or_404
from notifications.models import Notification



User = settings.AUTH_USER_MODEL

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")  # prevents duplicate likes

    def __str__(self):
        return f"{self.user} likes {self.post}"
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
    
    from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Like
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        # Check if like already exists
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # ✅ Create notification
            if post.author != request.user:  # don’t notify self-like
                Notification.objects.create(
                    recipient=post.author,
                    sender=request.user,
                    notification_type="like",
                    post=post,
                )
            return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
