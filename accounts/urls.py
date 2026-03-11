from django.urls import path
from .views import user_view 
urlpatterns=[
    path("form/",user_view,)
]