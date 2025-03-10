import pytest
import asyncio
import json
from unittest.mock import AsyncMock
from cryp_app.binance_ws import binance_websocket

@pytest.mark.asyncio
async def test_binance_websocket(mocker):
    """Тестирует обработку сообщений WebSocket от Binance"""

    # Создаём мок WebSocket-соединения
    mock_websocket = AsyncMock()
    
    # Используем итератор для side_effect, чтобы корректно вызывать .recv()
    mock_websocket.recv.side_effect = iter([
        asyncio.Future(),  # Первое сообщение
        asyncio.Future(),  # Второе сообщение
        asyncio.CancelledError(),  # Завершение цикла
    ])
    
    # Заполняем будущее значение
    mock_websocket.recv.side_effect.__next__().set_result(json.dumps({"s": "BTCUSDT", "p": "45000.00"}))
    mock_websocket.recv.side_effect.__next__().set_result(json.dumps({"s": "ETHUSDT", "p": "3200.00"}))

    # Мокаем websockets.connect
    mock_connect = mocker.patch("websockets.connect", return_value=AsyncMock())
    mock_connect.return_value.__aenter__.return_value = mock_websocket

    # Проверяем, что вызывается CancelledError (имитация выхода)
    with pytest.raises(asyncio.CancelledError):
        await binance_websocket()

