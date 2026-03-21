from django.urls import path
from .views import *
urlpatterns=[
    path("form/",user_view),
    path("category_new/",category_view,name='category_create'),
    path('category_update/',update_category),
    path('read/',read_category),
    path('delete/',delete_category,name="delete"),
    path('products/', product, name='product_page'),
    path('products/edit/<int:pk>/', edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', delete_product, name='delete_product'),
]