from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import Userform,Categoryform,Productform
from .models import User,Category,Product
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
def product(request):
    if request.method == "POST":
        form = Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_page')
    else:
        form = Productform()
    all_products = Product.objects.all()
    return render(request, "products.html", {'form': form, 'product': all_products})

def edit_product(request, pk):
    product_instance = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = Productform(request.POST, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('product_page') 
    else:

        form = Productform(instance=product_instance)
    return render(request, "edit_product.html", {'form': form, 'product_instance': product_instance})
def delete_product(request, pk):
    product_instance = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_instance.delete()     
        return redirect('product_page')
    return render(request, "delete_product.html", {'product_instance': product_instance})