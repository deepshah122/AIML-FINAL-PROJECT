#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf

from sklearn.metrics import accuracy_score


# Specify the stock symbol and market index symbol
stock_symbol = 'AAPL'  
market_index_symbol = 'NDAQ'  

# Download historical and current data for the stock and market index
stock_data = yf.Ticker(stock_symbol)
market_data = yf.Ticker(market_index_symbol)

# Get historical data for a specified time period
stock_history = stock_data.history(period="5y")  # Adjust the time period as needed
market_history = market_data.history(period="5y")  # Adjust the time period as needed

# Get the current stock price
current_stock_price = stock_data.history(period="1d")['Close'].iloc[0]

# Calculate daily returns for historical data
stock_returns = stock_history['Close'].pct_change().dropna()
market_returns = market_history['Close'].pct_change().dropna()

# Calculate the beta
covariance_matrix = stock_returns.cov(market_returns)
beta = covariance_matrix / market_returns.var()

# Calculate the standard deviation
stock_std_dev = stock_returns.std()

print(f"Current Stock Price of {stock_symbol}: ${current_stock_price:.2f}")

print(f"5-Year Beta of {stock_symbol}: {beta:.4f}")
print(f"5-Year Standard Deviation of {stock_symbol}: {stock_std_dev:.4f}")


# In[ ]:




