from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from .models import Book , Librarian , Author , UserProfile
from .models import Library
from django.contrib.auth import logout 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import user_passes_test , login_required
from django.contrib.auth.decorators import permission_required


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






# Check functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


# Views
@user_passes_test(is_admin, login_url='login')

def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_member, login_url='login')

def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_librarian, login_url='login')

def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')




@permission_required('relationship_app.can_add_book')
@login_required
def add_book_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        published_year = request.POST.get('published_year')

        if title and author_id and published_year:
            try:
                author = Author.objects.get(id=author_id)
                Book.objects.create(title=title, author=author, published_year=published_year)
                return redirect('list_books')
            except Author.DoesNotExist:
                pass

    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_change_book')
@login_required
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        published_year = request.POST.get('published_year')
        if title and published_year:
            book.title = title
            book.published_year = published_year
            book.save()
            return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
@login_required
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})