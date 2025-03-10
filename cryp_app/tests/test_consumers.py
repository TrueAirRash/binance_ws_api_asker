import pytest
import json
from channels.testing import WebsocketCommunicator
from cryp_proj.asgi import application

@pytest.mark.asyncio
async def test_websocket_server():
    """Тест WebSocket-сервера на факт получения данных в нужном формате"""
    
    # Подключаемся к WebSocket
    communicator = WebsocketCommunicator(application, "/ws/prices/")
    connected, _ = await communicator.connect()
    assert connected  # Проверяем, что соединение установлено
    
    # Получаем сообщение от сервера
    response = await communicator.receive_json_from(timeout=5)  # Ждем реальных данных
    
    # Проверяем, что ответ - это словарь с ожидаемыми ключами
    assert isinstance(response, dict), f"Ответ должен быть JSON, получено: {response}"
    assert "symbol" in response, "Нет ключа 'symbol' в ответе"
    assert "price" in response, "Нет ключа 'price' в ответе"

    # Проверяем, что цена - это число
    assert isinstance(response["price"], (int, float)), f"'price' должен быть числом, а не {type(response['price'])}"

