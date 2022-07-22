import pandas_datareader as pdr
import yfinance as yf
from web_scraper import StockScraper
import pprint
import postgres_connection

#print(StockScraper('nvda').scrape_yfinance())
#print(StockScraper('sq').scrape_yfinance())
#pprint.pprint(StockScraper('ibm').scrape_yfinance())
# print(StockScraper('V').scrape_yfinance())
# print(StockScraper('F').scrape_yfinance())

watch_list = ['nvda','ibm']

postgres_connection.insert_into_watchlist('f')
print(postgres_connection.select_query('select * from investment_tool.watch_list'))