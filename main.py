import pandas_datareader as pdr
import yfinance as yf
from web_scraper import StockScraper


# print(StockScraper('nvda').scrape_yfinance())
#
# print(StockScraper('sq').scrape_yfinance())
print(StockScraper('nvda').scrape_yfinance())
# print(StockScraper('V').scrape_yfinance())
# print(StockScraper('F').scrape_yfinance())
# print()
# print()