import yfinance as yf
from datetime import datetime, timedelta
from .models import Stock, StockPrice
from django.conf import settings

def fetch_stock_prices(stock_code):
    stock = yf.Ticker(stock_code)
    # Fetch historical data for the last week
    today = datetime.today().strftime('%Y-%m-%d')
    last_week = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    hist = stock.history(start=last_week, end=today)
    
    if not hist.empty:
        stock_obj, _ = Stock.objects.get_or_create(code=stock_code, defaults={'name': stock_code})
        
        for date, row in hist.iterrows():
            StockPrice.objects.update_or_create(
                stock=stock_obj, 
                date=date, 
                defaults={'price': row['Close']}
            )
        return True, "Stock prices imported successfully."
    else:
        return False, "No data fetched. Possible incorrect stock code or other issue."
