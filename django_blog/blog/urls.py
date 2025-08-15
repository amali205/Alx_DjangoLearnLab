from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login (uses built-in view + default template name)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Registration (custom view)
    path('register/', views.Register, name='register'),

    # Profile (custom view)
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),  # name='home' is important
    path('posts/', views.posts_list, name='posts'),  # name must be 'posts'


]
