from django import forms
from .models import User,Category

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
