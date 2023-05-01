from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',  'author', 'content']
        labels = {
            'title':"",
            'content':"",
            'author':"",
            # 'date_published':"",
        }
        widgets = {
            # 'date_published': forms.DateInput(attrs={'type': 'date', 'placeholder':'date published', 'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SuperheroJT'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your post'}),
        }
