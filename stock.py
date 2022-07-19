import yfinance


def return_stock_information(ticker):
    return yfinance.Ticker(str(ticker)).info['shortName']

