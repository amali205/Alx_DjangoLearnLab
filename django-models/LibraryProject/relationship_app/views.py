from django.shortcuts import render
from django.views.generic import ListView , DetailView
# Create your views here.



def book_list(request):
    return render(request,'List_books.html')

class BookListView(ListView):
 def get(self, request):
        return render(request, 'List_books.html')
class BookDetailView(DetailView):
 def get(self, request):
        return render(request, 'List_books.html')
