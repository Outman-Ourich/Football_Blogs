from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page,name="main"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.post,name="post")
    

]