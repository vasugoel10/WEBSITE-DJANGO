from django.urls import path
from .views import user_view,category_view ,update_category,read_category,delete_category
urlpatterns=[
    path("form/",user_view),
    path("category_new/",category_view,name='category_create'),
    path('category_update/',update_category),
    path('read/',read_category),
    path('delete/',delete_category,name="delete"),
]