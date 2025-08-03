from django.urls import path
from .views import   LibraryDetailView
from .views import list_books
from .views import BookListView
from .views import loginview
from .views import logoutview
from . import views



urlpatterns = [
       path('book_list1', BookListView.as_view(), name='book-listview'),
       path('book_list2', LibraryDetailView.as_view(), name='book-detail'),
       path('book_list3', list_books, name='book-list'),
       path('register', views.register , name= 'register'),
       path('login', loginview.as_view(template_name="relationship_app/login.html") , name='login'),
       path('logout',logoutview.as_view(template_name="relationship_app/logout.html")  , name='logout')
]
