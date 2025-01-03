# Import libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
import seaborn as sns

# Step 1: Download stock data
print("Downloading Apple stock data...")
stock_data = yf.download("AAPL", start="2015-01-01", end="2023-01-01")

# Step 2: Data Cleaning
stock_data.dropna(subset=['Close'], inplace=True)  # Remove rows with missing 'Close' values
print("Data cleaned successfully.")

# Step 3: Data Exploration
print(f"Stock data summary:\n{stock_data.describe()}")

# Step 4: Calculate Moving Average
stock_data['30_MA'] = stock_data['Close'].rolling(window=30).mean()

# Step 5: Visualize Close Prices with Moving Average
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price', color='blue', alpha=0.7)
plt.plot(stock_data['30_MA'], label='30-Day Moving Average', color='orange', linewidth=2)
plt.title("Apple Stock Price with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

# Step 6: Forecasting Using Exponential Smoothing
# Configure the model
model = ExponentialSmoothing(
    stock_data['Close'],
    trend='add',       # Additive trend
    seasonal='add',    # Additive seasonality
    seasonal_periods=365  # Assume annual seasonality
)

print("Training Exponential Smoothing model...")
fit = model.fit()

# Forecast the next 30 days
forecast_steps = 30
forecast = fit.forecast(steps=forecast_steps)

# Step 7: Plot Forecast vs Historical Prices
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Historical Prices', color='blue')
plt.plot(forecast, label='Forecasted Prices', color='red', linestyle='--', marker='o')
plt.title("Stock Price Forecast")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()
plt.show()

# Step 8: Evaluation Metrics (Optional)
from sklearn.metrics import mean_squared_error
historical = stock_data['Close'][-forecast_steps:]
forecast_trimmed = forecast[:len(historical)]  # Ensure alignment
rmse = mean_squared_error(historical, forecast_trimmed, squared=False)
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Step 9: Save Forecast Data
forecast_data = pd.DataFrame({
    'Date': pd.date_range(start=stock_data.index[-1], periods=forecast_steps + 1, freq='D')[1:],
    'Forecasted Price': forecast
})
forecast_data.to_csv("forecasted_prices.csv", index=False)
print("Forecast data saved to 'forecasted_prices.csv'.")
