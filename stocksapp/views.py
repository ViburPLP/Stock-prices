from django.shortcuts import render
import requests
from .models import StockPrice

def dashboard(request):
    api_key = "ZROA09JARY1NMF05"
    symbol = "AAPL"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()["Time Series (Daily)"]

    stock_prices = []
    for date, values in data.items():
        stock_price = StockPrice.objects.create(
            date=date,
            stock_symbol=symbol,
            price=values["4. close"]
        )
        stock_prices.append(stock_price)

    return render(request, 'stocks.html', {'stock_prices': stock_prices})
