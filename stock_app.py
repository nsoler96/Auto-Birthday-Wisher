import streamlit as st
import yfinance as yf
import pandas as pd

# Title of the web app
st.title("Stock Price Web Application")

# Input for the stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT):", "AAPL")

# Get stock data from Yahoo Finance
@st.cache
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period="1d", start="2020-01-01", end="2024-01-01")
    return stock_data

# Display stock data
if stock_symbol:
    data = get_stock_data(stock_symbol)
    st.subheader(f"Stock Data for {stock_symbol}")
    st.line_chart(data['Close'])
    st.write(data.tail())
