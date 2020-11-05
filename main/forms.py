from django import forms
from .models import Furniture

class PostAdForm(forms.ModelForm):

    class Meta:
        model = Furniture
        exclude = ('slug',)
