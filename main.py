import pandas_datareader as pdr
import yfinance as yf




msft = yf.Ticker("MSFT")

# get stock info
print(msft.history(period="max"))

