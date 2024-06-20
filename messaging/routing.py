from django.urls import path
from messaging.consumers import GroupChatConsumer, PrivateChatConsumer

websocket_urlpatterns = [
    path("" , GroupChatConsumer.as_asgi()) , 
    path('ws/chat/<str:username>/', PrivateChatConsumer.as_asgi()),
]
