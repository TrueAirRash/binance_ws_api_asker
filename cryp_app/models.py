from django.db import models

class CryptoPrice(models.Model):
    symbol = models.CharField(max_length=10)  # Тикер криптовалюты 
    price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена
    timestamp = models.DateTimeField(auto_now_add=True)  # Время обновления

    def str(self):
        return f"{self.symbol}: {self.price} at {self.timestamp}"
