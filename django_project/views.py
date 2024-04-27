import requests
from django.shortcuts import render
from .models import StockPrice


def fetch_stock_prices(request):
    api_key = "ZROA09JARY1NMF05"  
    symbol = "AAPL"  # Example stock symbol (Apple Inc.)
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
      # StockPrice(
        #     date=date,
        #     stock_symbol=symbol,
        #     price=values["4. close"]
        # )
    #     stock_price.save()

    # return render(request, 'your_template.html', {'message': 'Stock prices fetched and saved successfully!'})
