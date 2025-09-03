from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Notification(models.Model):
    recipient = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='sent_notifications')
    verb = models.CharField(max_length=255)  # e.g., 'liked', 'commented', 'followed'
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    actor = models.ForeignKey('accounts.CustomUser', null=True, blank=True, on_delete=models.CASCADE, related_name='actor_notifications')
    target = GenericForeignKey()    
    def __str__(self):
        return f"Notification to {self.recipient.username} from {self.sender.username} - {self.verb}"