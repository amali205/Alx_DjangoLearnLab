from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from .models import Book , Librarian , Author
from .models import Library
# Create your views here.



def list_books(request):
    return render(request,'relationship_app/list_books.html')

class BookListView(ListView):
 def get(self, request):
        return render(request, 'List_books.html', { 'books' :Book.objects.all()})
class LibraryDetailView(DetailView):
 def get(self, request):
        return render(request, 'relationship_app/library_detail.html' , Library.objects.all())
