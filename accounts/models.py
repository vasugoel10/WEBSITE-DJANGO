from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200,unique=True)
    phone=PhoneNumberField(unique=True)
    email=models.EmailField(max_length=320,unique=True)
# class Books(models.Model):
#     title=models.CharField(max_length=100)
#     author=models.CharField(max_length=200)
#     isbn_number=models.IntegerField(unique=True)
#     added_by=models.CharField(max_length=200)