from django.shortcuts import render , redirect
from django.urls import reverse_lazy
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







        
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # template file
    context_object_name = 'posts'
    

# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user  # link post to logged-in user
        return super().form_valid(form)

# Update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        return self.get_object().author == self.request.user