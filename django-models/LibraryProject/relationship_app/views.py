from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from .models import Book , Librarian , Author
from .models import Library
from django.contrib.auth import logout 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import user_passes_test


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
class LoginView(ListView):
    def get(self, request):
     login_form = login()    
     return render (request , 'relationship_app/login.html' ,  {"form": login_form})
class LogoutView(ListView):
     def get(self, request):
      logout(request)
      return render(request , 'logout.html' )


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')