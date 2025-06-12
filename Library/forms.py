from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'category', 'model_file', 'preview_image','published']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Post'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Post'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
