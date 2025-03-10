from django.urls import re_path
from .consumers import CryptoConsumer

websocket_urlpatterns = [
    re_path(r'ws/prices/', CryptoConsumer.as_asgi()),
]
