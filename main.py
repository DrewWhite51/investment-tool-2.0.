import yfinance
from web_scraper import StockScraper
import pprint
import postgres_connection
import stock
watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

# postgres_connection.compare_watchlist(watch_list)

ibm = stock.Stock('ibm').get_daily_technicals()

print(ibm)

#
# for data in get_data('ibm'):
#     print(data)
