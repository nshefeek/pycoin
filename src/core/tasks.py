from django.utils import timezone
from celery import shared_task
import requests
from .models import Quote
API_URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=W197OVAPVSAHLL4I"

@shared_task(name='fetch-price')
def fetch_price():
    data = requests.get(API_URL).json()
    print(data)
    from_currency = data['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_currency = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
    exchange = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    last_refreshed = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
    print(type(last_refreshed))
    Quote.objects.create(
        from_currency = from_currency,
        to_currency = to_currency,
        exchange = exchange,
        last_refreshed = last_refreshed,
    )