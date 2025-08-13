from django.urls import path ,include
from .router import router
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView
urlpatterns = [
    path('all_books' , ListView.as_view() ,name='all_book'),
    path('books/<int:pk>', DetailView.as_view() ,name='book'),
    path('books/create', CreateView.as_view(),name='creat' ),  
    path('books/update' , UpdateView.as_view() , name= 'update'),
    path('books/delete' ,DeleteView.as_view() , name='delete'),
    path('', include(router.urls))
]



