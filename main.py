import pandas_datareader as pdr
import yfinance as yf
from web_scraper import StockScraper
import pprint

#print(StockScraper('nvda').scrape_yfinance())
#print(StockScraper('sq').scrape_yfinance())
pprint.pprint(StockScraper('ibm').scrape_yfinance())
# print(StockScraper('V').scrape_yfinance())
# print(StockScraper('F').scrape_yfinance())
# print()
# print()