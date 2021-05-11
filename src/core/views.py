from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from .serializers import QuoteSerializer
from .models import Quote

API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=W197OVAPVSAHLL4I"

# Create your views here.
class QuoteView(APIView):
    def get(self, *args, **kwargs):
        data = requests.get(API_URL)
        return Response(data.json())

    def post(self, request, *args, **kwargs):
        return Response({"test": "Test success"})