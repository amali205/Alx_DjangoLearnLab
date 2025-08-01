from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Book , Librarian , Author
from .models import Library
# Create your views here.



def book_list(request):
    return render(request,r'relationship_app/list_books.html')

class BookListView(ListView):
 def get(self, request):
        return render(request, 'List_books.html', { 'books' :Book.objects.all()})
class BookDetailView(DetailView):
 def get(self, request):
        return render(request, 'library_detail.html' , Library.objects.all())
