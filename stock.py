import yfinance


def return_stock_information(ticker):
    return yfinance.Ticker(str(ticker)).info['shortName']


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_stock_name(self):
        try:
            return yfinance.Ticker(self.ticker).info['shortName']
        except NameError:
            return 'Name not found'
