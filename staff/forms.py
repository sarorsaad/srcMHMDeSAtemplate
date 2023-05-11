from django import forms
from .models import CRUD

class CRUDForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"})
    )
    age = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Age"})
    )
    level = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Level"})
    )

    class Meta:
        model = CRUD
        fields = ['name', 'age', 'level']
