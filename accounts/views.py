from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import Userform,Categoryform
from .models import User,Category
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
def category_view(request):
    if request.method=="POST":
        form=Categoryform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Categoryform()
    return render(request,'category.html',{'form':form})

def update_category(request):
    categories = Category.objects.all()
    selected_category = None
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "form1":
            category_id = request.POST.get("category_id")
            selected_category = Category.objects.get(id=category_id)
        elif form_type == "update":
            category_id = request.POST.get("category_id")
            name = request.POST.get("name")
            description = request.POST.get("description")
            category = Category.objects.get(id=category_id)
            category.name = name
            category.description = description
            category.save()
            selected_category = category
    return render(request, "update.html", {
        "data": categories,
        "selected_category": selected_category
    })
def read_category(request):
    cat=Category.objects.all()
    return render(request,"read.html",{"cat":cat})


def delete_category(request):
    
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            return redirect('delete')
    categories = Category.objects.all()
    context = {'categories': categories}
    
    return render(request, 'delete.html', context)