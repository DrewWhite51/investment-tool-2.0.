import cryptocompare

import postgres_connection
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
import candlestick_bot

watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']

ibm = stock.Stock('ibm')
btc = crypto.Crypto('BTC')
nvda = stock.Stock('NVDA')

# for data in btc.get_hourly_historical():
#     # print(data)
#     dt_object = datetime.fromtimestamp(data['time']).strftime("%m/%d/%Y, %H:%M:%S")
#     print(dt_object, data['close'])

# pprint.pprint(cryptocompare.get_exchanges())

print(ibm.get_daily_technicals())
postgres_connection.write_daily_ohlc(ibm)

# print(grapher.Grapher('ibm').graph_candlesticks())
#
# print(parser.parse_daily_technicals('ibm')[0:10])

#
# def write_daily_ohlc(stock_obj):
#
#     stock_obj.get_daily_technicals().to_csv(f'{stock_obj.get_ticker()}.csv')
#
#     file = f'{stock_obj.get_ticker()}.csv'
#
#     with open(file, 'r') as csvfile:
#         start = time.time()
#         datareader = csv.reader(csvfile)
#         for row in datareader:
#             print(row)
#         end = time.time()
#         print(end - start)
#
#     os.remove(f'{stock_obj.get_ticker()}.csv')
#
#
# print(write_daily_ohlc(nvda))
