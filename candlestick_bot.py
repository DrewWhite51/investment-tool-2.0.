

class CandlestickReader:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def return_candles(self):
        open = self.dataframe['open']
        high = self.dataframe['high']
        print(len(open), (high))

    def bullish_swing(self):
        pass