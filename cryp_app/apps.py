from django.apps import AppConfig
import threading
import asyncio

class CrypAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cryp_app'

    def ready(self):
        """Запускает WebSocket-клиент Binance при старте Django."""
        from cryp_app.binance_ws import binance_websocket
        
        def start_ws_client():
            asyncio.run(binance_websocket())

        # Запуск в отдельном потоке, чтобы не блокировать Django
        thread = threading.Thread(target=start_ws_client, daemon=True)
        thread.start()
