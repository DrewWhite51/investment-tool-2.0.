import cryptocompare
from web_scrapers import coin_desk_scraper
import stock
from web_scrapers import yfinance_scraper
import csv
import time
import os
import parser
import crypto
import pprint
from datetime import datetime
import grapher


watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

ibm = stock.Stock('ibm')
btc = crypto.Crypto('BTC')

# for data in btc.get_hourly_historical():
#     # print(data)
#     dt_object = datetime.fromtimestamp(data['time']).strftime("%m/%d/%Y, %H:%M:%S")
#     print(dt_object, data['close'])

# pprint.pprint(cryptocompare.get_exchanges())

# print(ibm.get_daily_technicals()['open'])

# print(grapher.Grapher('ibm').graph_candlesticks())

cd = coin_desk_scraper.CoinDeskScraper().home_page_scraper()

print(cd)