from django.urls import path
from .views import CryptoPriceListView, index

urlpatterns = [
    path('', index, name='home'),  # Тут возможность открыть по http://127.0.0.1:8000
    path('prices/', CryptoPriceListView.as_view(), name='price-list'),
]
