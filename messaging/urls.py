from django.urls import path
# from .views import GetQuestionAll, GetQuestion, GetQuestionAllSrc, GetQuestionSrcChapter
from .views import *


urlpatterns = [
    path("private/", private_chat_list, name="private_chat_list"),
    path("private/<username>/", private_chat_page, name="private_chat_page"),
    path("group/", group_chat_page, name="group_chat_page"),
]