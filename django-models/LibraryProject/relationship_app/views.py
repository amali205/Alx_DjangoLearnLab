from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from .models import Book , Librarian , Author
from .models import Library
from django.contrib.auth import  logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.



def list_books(request):
    return render(request,'relationship_app/list_books.html')

class BookListView(ListView):
 def get(self, request):
        return render(request, 'relationship_app/List_books.html', {"books":Book.objects.all()})
class LibraryDetailView(DetailView):
 def get(self, request):
        return render(request, 'relationship_app/library_detail.html' , {"books":Library.objects.all()})

def register(request):
    form = UserCreationForm()
    return render(request , 'relationship_app/register.html' , {"form":form})
def loginform(request):
    login_form = AuthenticationForm()    
    return render (request , 'relationship_app/login.html' ,  {"form": login_form})
def logoutform(request):
    logout(request)
    return render(request , 'relationship_app/logout.html' )