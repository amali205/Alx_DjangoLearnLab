from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CreateView ,DeleteView ,DetailView ,ListView , UpdateView
urlpatterns = [
    # Login (uses built-in view + default template name)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Registration (custom view)
    path('/', views.Register, name='register'),

    # Profile (custom view)
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),  # name='home' is important
    path('posts/', views.posts_list, name='posts'),  # name must be 'posts'


    path('', ListView.as_view(), name='posts'),  
    path('blog/posts/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),


]
