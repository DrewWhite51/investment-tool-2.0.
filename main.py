import cryptocompare

import stock
from web_scrapers import yfinance_scraper
import csv
import time
import os
import parser
import crypto
import pprint
from datetime import datetime
watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

btc = crypto.Crypto('BTC')

# for data in btc.get_hourly_historical():
#     # print(data)
#     dt_object = datetime.fromtimestamp(data['time']).strftime("%m/%d/%Y, %H:%M:%S")
#     print(dt_object, data['close'])

# pprint.pprint(cryptocompare.get_exchanges())


