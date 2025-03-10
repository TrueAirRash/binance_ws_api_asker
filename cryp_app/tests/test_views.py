import pytest
from django.urls import reverse
from cryp_app.models import CryptoPrice

@pytest.mark.django_db
def test_price_list_view(client):
    # Внести тестовую запись
    CryptoPrice.objects.create(symbol="BTCUSDT", price=45000.00)

    # Тестовый GET-запрос к API
    response = client.get(reverse("price-list"))
    assert response.status_code == 200

    # Получить данные из ответа
    response_data = response.json()

    # Проверка на то, что пришла 1 запись
    assert len(response_data) == 1

    # Проверка корректности записи
    assert response_data[0]["symbol"] == "BTCUSDT"
    assert float(response_data[0]["price"]) == 45000.00
