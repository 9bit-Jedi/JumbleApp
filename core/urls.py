from django.urls import path
# from . import views
from .views import register
from posts.views import post_list

urlpatterns = [
    path("", post_list , name="post_list"),
    path("register", register , name="register"),
]