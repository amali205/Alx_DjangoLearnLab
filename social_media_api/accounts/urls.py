from django.urls import path , include
    
from .views import UserViewSet , RegisterView , loginView , meview

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', loginView.as_view(), name='login'),
   path('me/', meview.as_view(), name='me'),
   Add follow/unfollow paths here if you have corresponding views, for example:
   path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
   path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
   path('users/', include((UserViewSet.as_view({'get': 'list'}), 'users'), namespace='users')),

]

