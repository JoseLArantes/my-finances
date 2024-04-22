import requests
from datetime import datetime, timedelta
from .models import Stock, StockPrice
from django.conf import settings

def fetch_stock_prices(stock_code):
    API_KEY = settings.ALPHA_VANTAGE_API_KEY  # This should be configured in your settings.py
    URL = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_code,
        "apikey": API_KEY
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    data = response.json()

    if "Time Series (Daily)" in data:
        time_series = data["Time Series (Daily)"]
        stock, _ = Stock.objects.get_or_create(code=stock_code)

        # Import prices for the last week
        for date_str, price_data in time_series.items():
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date >= datetime.now() - timedelta(days=7):
                price = float(price_data['4. close'])  # Use closing price
                StockPrice.objects.update_or_create(stock=stock, date=date, defaults={'price': price})
        return True, "Stock prices imported successfully."
    return False, "Error fetching stock prices or invalid data format."
