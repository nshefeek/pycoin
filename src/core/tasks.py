from celery import shared_task
import requests
from .models import Quote
import os

API_KEY = os.getenv("API_KEY")
API_URL = "https://www.alphavantage.co/query"
PARAMETERS = {
            "function": function,
            "from_currency": "BTC",
            "to_currency": "USD",
            "apikey": API_KEY,
        }

@shared_task(name='fetch-price')
def fetch_price():
    data = requests.get(API_URL, params=PARAMETERS).json()

    from_currency = data['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_currency = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
    exchange = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    last_refreshed = data['Realtime Currency Exchange Rate']['6. Last Refreshed']

    Quote.objects.create(
        from_currency = from_currency,
        to_currency = to_currency,
        exchange = exchange,
        last_refreshed = last_refreshed,
    )
