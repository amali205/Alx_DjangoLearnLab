from django.urls import path
from .views import   LibraryDetailView
from .views import list_books
from .views import BookListView
from .views import LoginView
from .views import LogoutView
from . import views
from .views import admin_view , member_view , librarian_view , add_book_view, edit_book_view, delete_book_view


urlpatterns = [
       path('book_list1', BookListView.as_view(), name='book-listview'),
       path('book_list2', LibraryDetailView.as_view(), name='book-detail'),
       path('book_list3', list_books, name='book-list'),
       path('register', views.register , name= 'register'),
       path('login', LoginView.as_view(template_name="relationship_app/login.html") , name='login'),
       path('logout',LogoutView.as_view(template_name="relationship_app/logout.html")  , name='logout'),
       path('librarian-role/', librarian_view, name='librarian_view'),
       path('member-role/', member_view, name='member_view'),   
       path('add_book/', add_book_view, name='add_book'),
       path('edit_book/<int:book_id>/', edit_book_view, name='edit_book'),
       path('delete_book/<int:book_id>/', delete_book_view, name='delete_book'),
]

