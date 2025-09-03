from django.urls import path
from .views import NotificationListView , MarkAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('mark-as-read/<int:pk>/', MarkAsReadView.as_view(), name='mark-as-read'),

]