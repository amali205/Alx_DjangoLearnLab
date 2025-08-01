from django.urls import path
from .views import  list_books, LibraryDetailView
from .views import BookListView


urlpatterns = [
       path('book_list1', BookListView.as_view(), name='book-list'),
       path('book_list2', LibraryDetailView.as_view(), name='book-detail'),
       path('book_list3', list_books, name='book-list'),
]
