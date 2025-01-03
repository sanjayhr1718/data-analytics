import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

stock_data = yf.download("AAPL", start="2015-01-01", end="2023-01-01")

stock_data.dropna(subset=['Close'], inplace=True)

stock_data['30_MA'] = stock_data['Close'].rolling(window=30).mean()

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['30_MA'], label='30-Day Moving Average', color='orange')
plt.title("Stock Price Trend with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

model = ExponentialSmoothing(stock_data['Close'], trend='add', seasonal='add', seasonal_periods=365)
fit = model.fit()
forecast = fit.forecast(steps=30)

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Historical Prices')
plt.plot(forecast, label='Forecasted Prices', color='red')
plt.title("Stock Price Forecast")
plt.legend()
plt.grid()
plt.show()
