from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=W197OVAPVSAHLL4I"

# Create your views here.
class QuoteView(APIView):
    def get(self, *args, **kwargs):
        data = requests.get(API_URL)
        print(data.json())
        return JsonResponse(data.json())

    def post(self, *args, **kwargs):
        return JsonResponse({"test": "Test success"})