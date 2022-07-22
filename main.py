import pandas_datareader as pdr
import yfinance as yf
from web_scraper import StockScraper
import pprint
import postgres_connection

# print(StockScraper('nvda').scrape_yfinance())

watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

postgres_connection.compare_watchlist(watch_list)
