from django import forms
from .models import Post

class CRUDForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Title"
    }))
    post_type = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Post Type"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Description"
    }))
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ['title', 'post_type', 'description', 'image']
