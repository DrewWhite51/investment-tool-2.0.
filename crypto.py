import cryptocompare
import datetime


class Crypto:

    def __init__(self, ticker):
        self.ticker = ticker

    def return_price(self):
        return cryptocompare.get_price(f'{self.ticker}', 'USD')

    def get_daily_historical(self):
        return cryptocompare.get_historical_price_day(f'{self.ticker}', 'USD')

    def get_hourly_historical(self):
        return cryptocompare.get_historical_price_hour(f'{self.ticker}', 'USD')

    def get_minute_historical(self):
        return cryptocompare.get_historical_price_minute(f'{self.ticker}', 'USD')
