# import asyncio
# import json
# import websockets
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from django.utils.timezone import now
# from .models import CryptoPrice

# BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# async def save_price(data):
#     """Сохранение цены в базе данных"""
#     symbol = data.get("s")
#     price = float(data.get("p"))

#     await CryptoPrice.objects.acreate(symbol=symbol, price=price, timestamp=now())

#     # Рассылаем обновления клиентам Django Channels
#     channel_layer = get_channel_layer()
#     event = {
#         "type": "send_price_update",
#         "data": {"symbol": symbol, "price": price}
#     }
#     await channel_layer.group_send("crypto_prices", event)

# async def binance_websocket():
#     """Подключение к Binance WebSocket API"""
#     async with websockets.connect(BINANCE_WS_URL) as websocket:
#         while True:
#             response = await websocket.recv()
#             data = json.loads(response)
#             await save_price(data)


import datetime
import asyncio
import json
import websockets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.timezone import now
from .models import CryptoPrice

BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

latest_price = None
last_saved_time = None

async def save_price(symbol, price):
    """Сохранение цены в базе данных раз в 15 секунд"""
    global last_saved_time
    current_time = now()

    if last_saved_time is None or (current_time - last_saved_time).total_seconds() >= 15:
        await CryptoPrice.objects.acreate(symbol=symbol, price=price, timestamp=current_time)
        last_saved_time = current_time

async def binance_websocket():
    """Подключение к Binance WS API"""
    async with websockets.connect(BINANCE_WS_URL) as websocket:
        global latest_price
        while True:
            response = await websocket.recv()
            
            # Является ли response строкой
            if not isinstance(response, str):
                response = response.decode("utf-8")  # Если пришел байтовый объект

            data = json.loads(response)  
            symbol = data.get("s")
            price = float(data.get("p"))
            latest_price = price

            # Рассылка обновления клиентам Django Channels
            channel_layer = get_channel_layer()
            event = {
                "type": "send_price_update",
                "data": {"symbol": symbol, "price": price}
            }
            await channel_layer.group_send("crypto_prices", event)

            # Сохранение  цену раз в 15 секунд
            await save_price(symbol, price)

            
            
