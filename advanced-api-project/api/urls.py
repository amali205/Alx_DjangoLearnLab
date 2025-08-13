from django.urls import path ,include
from .router import router
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView
urlpatterns = [
    path('all_books' ,ListView.as_view() ,name='all_book'),
    path('all_books/<int:pk>', DetailView.as_view() ,name='book'),
    path('', include(router.urls))
]



