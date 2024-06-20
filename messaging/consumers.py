import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GroupChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.roomGroupName = "group_chat"
    await self.channel_layer.group_add(
      self.roomGroupName ,
      self.channel_name
    )
    await self.accept()
  async def disconnect(self , close_code):
    await self.channel_layer.group_discard(
      self.roomGroupName , 
      self.channel_layer 
    )
  async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json["message"]
    username = text_data_json["username"]
    await self.channel_layer.group_send(
      self.roomGroupName,{
        "type" : "sendMessage" ,
        "message" : message , 
        "username" : username ,
      })
  async def sendMessage(self , event) : 
    message = event["message"]
    username = event["username"]
    await self.send(text_data = json.dumps({"message":message ,"username":username}))


class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_username = self.scope['url_route']['kwargs']['username']
        self.room_group_name = f'chat_{self.other_username}_{self.scope["user"].username}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        receiver = text_data_json['receiver']  # Add receiver's username

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'receiver': receiver
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        receiver = event['receiver']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'receiver': receiver
        }))
