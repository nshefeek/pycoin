from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import os
from .serializers import QuoteSerializer
from .models import Quote

API_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("API_KEY")

class QuoteView(APIView):
    def get(self, *args, **kwargs):
        quote = Quote.objects.latest('last_refreshed')
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        function = "CURRENCY_EXCHANGE_RATE"
        from_currency = request.query_params.get("from_currency")
        to_currency = request.query_params.get("to_currency")

        parameters = {
            "function": function,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "apikey": API_KEY,
        }

        data = requests.get(API_URL, params=parameters)
        return Response(data.json())
