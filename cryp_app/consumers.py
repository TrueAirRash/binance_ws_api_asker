import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("crypto_prices", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("crypto_prices", self.channel_name)

    async def send_price_update(self, event):
        """Отправка данных клиенту"""
        data = event["data"]

        if isinstance(data, dict) and "symbol" in data and "price" in data:
            await self.send(text_data=json.dumps(data))

