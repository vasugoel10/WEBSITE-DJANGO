from django import forms
from .models import User,Category,Product

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
