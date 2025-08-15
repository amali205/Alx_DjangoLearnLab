from django.shortcuts import render , redirect
from django.contrib.auth import login , logout 
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login')
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







        



