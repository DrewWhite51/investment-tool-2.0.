import yfinance


def return_stock_information(ticker):
    return yfinance.Ticker(str(ticker)).info['shortName']


class Calculator:

    def get_sma(self, close_arr, days):
        pass






class Stock:
    pass

    def __init__(self, ticker):
        self.ticker = ticker

    def return_stock_information(self):
        return yfinance.Ticker(self.ticker.info['shortName'])

    def get_daily_technicals(self):
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        candles = yfinance.Ticker(self.ticker).history(period='max', interval='1d')
        close = candles['Close']
        open = candles['Open']
        high = candles['High']
        low = candles['Low']
        volume = candles['Volume']
        dates = []
        # print(candles.index)
        for data in candles.index:
            dates.append((data.to_pydatetime()).strftime('%Y/%m/%d, %H:%M:%S'))

        def get_sma(x):
            windows = close.rolling(x)
            sma = windows.mean()
            sma_list = []
            for sma_data in sma:
                sma_list.append(sma_data)
            return sma_list

        def get_ema(x):
            ema = close.ewm(span=x, adjust=False).mean()
            ema_list = []
            for ema_data in ema:
                ema_list.append(ema_data)
            return ema_list

        def get_upper_bollinger_band():
            closes = close
            sma = closes.rolling(20).mean()
            std = closes.rolling(20).std()
            bollinger_upper = sma + (std * 2)
            return bollinger_upper

        def get_lower_bollinger_band():
            sma = close.rolling(20).mean()
            std = close.rolling(20).std()
            bollinger_lower = sma - (std * 2)
            return bollinger_lower

        def get_rsi(periods=14):
            close_delta = close.diff()
            up = close_delta.clip(lower=0)
            down = -1 * close_delta.clip(upper=0)
            ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            rsi = ma_up / ma_down
            rsi = 100 - (100 / (1 + rsi))
            return rsi

        def get_stochastic_oscillator_k():
            fourteen_day_high = high.rolling(14).max()
            fourteen_day_low = low.rolling(14).max()
            K = (close - fourteen_day_low) * 100 / (fourteen_day_high - fourteen_day_low)
            K.rolling(3).mean()
            return K

        def get_stochastic_oscillator_d():
            fourteen_day_high = high.rolling(14).max()
            fourteen_day_low = low.rolling(14).max()
            K = (close - fourteen_day_low) * 100 / (fourteen_day_high - fourteen_day_low)
            D = K.rolling(3).mean()
            return D

        def get_macd():
            k = close.ewm(span=12, adjust=False).mean()
            d = close.ewm(span=26, adjust=False).mean()
            macd = k - d
            return macd

        def get_macd_s():
            k = close.ewm(span=12, adjust=False).mean()
            d = close.ewm(span=26, adjust=False).mean()
            macd = k - d
            macd_s = macd.ewm(span=9, adjust=False).mean()
            return macd_s

        def get_macd_h():
            k = close.ewm(span=12, adjust=False).mean()
            d = close.ewm(span=26, adjust=False).mean()
            macd = k - d
            macd_s = macd.ewm(span=9, adjust=False).mean()
            macd_h = macd - macd_s
            return macd_h

        print(get_sma(10))

        data = {
            'open': open,
            'high': high,
            'close': close,
            'low': low,
            'volume': volume,
            '5sma': get_sma(5),
            '7sma': get_sma(7),
            '10sma': get_sma(10),
            '21sma': get_sma(21),
            '50sma': get_sma(50),
            '100sma': get_sma(100),
            '200sma': get_sma(200),
            '5ema': get_ema(5),
            '7ema': get_ema(7),
            '9ema': get_ema(9),
            '13ema': get_ema(13),
            '12ema': get_ema(12),
            '26ema': get_ema(26),
            '48.5ema': get_ema(48.5),
            '50ema': get_ema(50),
            '100ema': get_ema(100),
            '200ema': get_ema(200),
            'upperBollingerBand': get_upper_bollinger_band(),
            'lowerBollingerBand': get_lower_bollinger_band(),
            'rsi': get_rsi(periods=14),
            'stochasticOscillatorK': get_stochastic_oscillator_k(),
            'stochasticOscillatorD': get_stochastic_oscillator_d(),
            'macd': get_macd(),
            'macdS': get_macd_s(),
            'macdH': get_macd_h()
        }
        # return data

    def get_hourly_data(self):
        return yfinance.Ticker(self.ticker).history(period='1y', interval='1h')

    def get_30m_data(self):
        return yfinance.Ticker(self.ticker).history(period='1mo', interval='30m')

    def get_min_data(self):
        return yfinance.Ticker(self.ticker).history(period='5d', interval='1m')

    def get_fundamental_data(self):
        stock = yfinance.Ticker(self.ticker)
        data = {
            'financials': stock.get_financials(),
            'info': stock.get_info(),
            'major_holders': stock.get_major_holders(),
            'instituional_holders': stock.get_institutional_holders(),
            'balance_sheet': stock.get_balance_sheet(),
            'quarterly_balance_sheet': stock.quarterly_financials,
            'cashflow': stock.get_cashflow(),
            'earnings': stock.get_earnings()
        }

        return data
