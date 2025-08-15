from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .models import Comment




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