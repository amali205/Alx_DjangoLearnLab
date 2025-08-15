from django.shortcuts import render , redirect
from django.contrib.auth import login , logout 
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def posts_list(request):
    return render(request, 'blog/posts.html')







        
class ListView(ListView):   # display all blog posts
        model = Post
        template_name = 'blog/posts.html'


class DetailView(DetailView): # show individual blog posts
        model = Post
        template_name = 'blog/posts.html'


class CreateView(CreateView, LoginRequiredMixin): # allow authenticated users to create new posts
        model = Post
        fields='__all__'
        template_name = 'blog/posts.html'


class UpdateView(UpdateView , LoginRequiredMixin ,UserPassesTestMixin): # enable post authors to edit their posts
        model = Post
        fields='__all__'
        template_name = 'blog/posts.html'



class DeleteView(DeleteView , LoginRequiredMixin , UserPassesTestMixin): # let authors delete their posts
        model = Post
        fields='__all__'
        template_name = 'blog/posts.html'

