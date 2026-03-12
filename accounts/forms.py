from django import forms
from .models import User,Books

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'

