from django.shortcuts import render

from rest_framework import generics
from .models import CryptoPrice
from .serializers import CryptoPriceSerializer

def index(request):
    return render(request, "cryp_app/index.html")

class CryptoPriceListView(generics.ListAPIView):
    queryset = CryptoPrice.objects.all().order_by('-timestamp')[:100]  # Последние 100 записей
    serializer_class = CryptoPriceSerializer
