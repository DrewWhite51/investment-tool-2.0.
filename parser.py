import time
import csv
import os
import stock

def parse_daily_technicals(ticker):

    analysis_stock = stock.Stock(ticker)

    technicals = analysis_stock.get_daily_technicals()

    technicals.to_csv(f'{analysis_stock.get_ticker()}.csv')

    file = (f'{analysis_stock.get_ticker()}.csv')

    with open(file, 'r') as csvfile:
        start = time.time()
        datareader = csv.reader(csvfile)
        for row in datareader:
            print(row)
        end = time.time()
        print(end - start)

    os.remove(f'{analysis_stock.get_ticker()}.csv')
