from django.urls import path
# from .views import GetQuestionAll, GetQuestion, GetQuestionAllSrc, GetQuestionSrcChapter
from .views import chatPage
from messaging.consumers import ChatConsumer


urlpatterns = [
    path("", chatPage, name="chatPage"),
]