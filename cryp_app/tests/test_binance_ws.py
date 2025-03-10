import pytest
import json
from unittest.mock import AsyncMock, patch
from cryp_app.binance_ws import binance_websocket

@pytest.mark.asyncio
async def test_binance_websocket():
    mock_websocket = AsyncMock()
    
    # Симуляция JSON-ответ от Binance
    mock_response = json.dumps({"e": "trade", "p": "50000.00"})  # Пример ответа
    
    mock_websocket.recv = AsyncMock(return_value=mock_response)  # Мок recv()

    # Добавление async with
    mock_connect = AsyncMock()
    mock_connect.__aenter__.return_value = mock_websocket
    mock_connect.__aexit__.return_value = AsyncMock()

    with patch('websockets.connect', return_value=mock_connect):
        await binance_websocket()
        mock_websocket.recv.assert_awaited()  # Проверяем, что recv() вызван

