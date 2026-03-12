from django.shortcuts import render
from .forms import Userform
from .models import User
# Create your views here.
def user_view(request):
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Userform()
    users = User.objects.all()
    return render(request,'user.html',{'form':form,'users':users})
# def book_view(request):
#     if request.method=="POST":
#         form=Bookform(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=Bookform()
#     users = User.objects.all()
#     return render(request,'user.html',{'form':form,'users':users})