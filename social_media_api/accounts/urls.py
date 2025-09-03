from django.urls import path , include
    
from .views import UserViewSet , RegisterView , loginView , meview

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', loginView.as_view(), name='login'),
   path('me/', meview.as_view(), name='me'),

]

