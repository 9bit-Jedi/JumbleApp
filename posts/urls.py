from django.urls import path
from .views import *

urlpatterns = [
    path("", post_list , name="post_list"),
    path("create-post", create_post , name="create_post"),
    path("edit-post/<post_id>", edit_post , name="edit_post"),
    path("delete-post/<post_id>", delete_post , name="delete_post"),
]