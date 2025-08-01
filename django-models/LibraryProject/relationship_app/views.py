from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Book
# Create your views here.



def book_list(request):
    return render(request,'List_books.html' , )

class BookListView(ListView):
 
 def get(self, request):
        return render(request, 'List_books.html', { 'books' :Book.objects.all()})
class BookDetailView(DetailView):
 def get(self, request):
        return render(request, 'List_books.html')
