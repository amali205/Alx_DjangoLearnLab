from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import     CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.Register, name='register'),

    # Profile
    path('profile/', views.profile, name='profile'),

    # Home
    path('', views.home, name='home'),

    # Posts CRUD
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),


     # Create
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    # Update
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    # Delete
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


    path('search/', views.search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
]


