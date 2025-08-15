from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .models import Comment , Tag , Post




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # we don't include post/author — set in view
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }
        labels = {
            'content': 'Your Comment'
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return content        
    




class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        tag_names = self.cleaned_data['tags']
        if tag_names:
            tag_list = [t.strip() for t in tag_names.split(',')]
            for tag_name in tag_list:
                tag_obj, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag_obj)
        return post    