import stock
from web_scrapers import yfinance_scraper
import csv
import time
import os
import parser


watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

# postgres_connection.compare_watchlist(watch_list)

# print(yfinance_scraper.StockScraper('ibm').scrape_yfinance())


stock = stock.Stock('nvda')

parser.parse_daily_technicals(stock.get_ticker())


