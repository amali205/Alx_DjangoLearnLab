from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # show unread first, then newest
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by('is_read', '-created_at')

class MarkAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.recipient != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to mark this notification.")
        return obj

    def perform_update(self, serializer):
        serializer.save(is_read=True)





