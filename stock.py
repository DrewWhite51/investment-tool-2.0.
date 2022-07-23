import yfinance


def return_stock_information(ticker):
    return yfinance.Ticker(str(ticker)).info['shortName']


class Stock:
    pass

    def __init__(self, ticker):
        self.ticker = ticker

    def return_stock_information(self):
        return yfinance.Ticker(self.ticker.info['shortName'])

    def get_daily_data(self):
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        return yfinance.Ticker(self.ticker.history(period='10y', interval='1d'))

    def get_hourly_data(self):
        return yfinance.Ticker(self.ticker.history(period='1y', interval='1h'))

    def get_30m_data(self):
        return yfinance.Ticker(self.ticker.history(period='1mo', interval='30m'))

    def get_min_data(self):
        return yfinance.Ticker(self.ticker.history(period='5d', interval='1m'))

    def get_fundamental_data(self):
        stock = yfinance.Ticker(self.ticker)
        financials = stock.get_financials()
        info = stock.get_info()
        major_holders = stock.get_major_holders()
        insitutional_holders = stock.get_institutional_holders()
        balance_sheet = stock.get_balance_sheet()
        quarterly_balance_sheet = stock.quarterly_financials
        cashflow = stock.get_cashflow()
        earnings = stock.get_earnings()
        news = stock.news
        news
