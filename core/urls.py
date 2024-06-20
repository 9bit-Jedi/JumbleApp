from django.urls import path
# from . import views
from .views import register, user_login, profile, user_logout, edit_profile
from posts.views import post_list

urlpatterns = [
    path("", post_list , name="post_list"),
    path("register", register , name="register"),
    path("login", user_login , name="user_login"),
    path("logout", user_logout , name="user_logout"),
    path("profile", profile , name="profile"),
    path("edit_profile", edit_profile , name="edit_profile"),
]