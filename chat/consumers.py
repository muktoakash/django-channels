"""chat/consumers.py"""

import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """consumer class for chat app"""
    async def __init__(self):
        AsyncWebsocketConsumer.__init__()
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code): # changed close_code to code
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data, bytes_data=None): 
        # added bytes_data argument to match superclass
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        """handles messages sent in chat"""
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))
