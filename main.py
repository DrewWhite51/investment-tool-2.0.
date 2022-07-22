import pandas_datareader as pdr
import yfinance as yf
from web_scraper import StockScraper
import pprint
import postgres_connection

# print(StockScraper('nvda').scrape_yfinance())

watch_list = ['nvda', 'ibm', 'f', 'v', 'voo', 'spy']


# postgres_connection.insert_into_watchlist('f')
# print(postgres_connection.select_query('select * from investment_tool.watch_list'))

def compare_watchlist(list_of_tickers):
    first_set = set(list_of_tickers)
    db_arr = []

    for db_tickers in (postgres_connection.select_query('select * from investment_tool.watch_list')):
        db_arr.append(db_tickers[0])

    for differences in first_set.difference(db_arr):
        print(f'Adding {differences} to the database.')
        postgres_connection.insert_into_watchlist(differences)


compare_watchlist(watch_list)
