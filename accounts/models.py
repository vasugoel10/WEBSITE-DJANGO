from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    phone=PhoneNumberField()
    email=models.EmailField(max_length=320)
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    description =models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    price=models.IntegerField(null=False)
    stock=models.IntegerField(default=0,null=False)
    def __str__(self):
        return self.name