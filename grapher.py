import plotly.graph_objects as go
from plotly.subplots import make_subplots
import stock


class Grapher:

    def __init__(self, ticker):
        self.ticker = ticker

    def graph_candlesticks(self):

        stock_obj = stock.Stock(self.ticker)
        length = 365
        dataframe = stock_obj.get_daily_technicals()
        fig = go.Figure(data=[go.Candlestick(
            x=dataframe.index[-length:],
            open=dataframe['open'][-length:],
            high=dataframe['high'][-length:],
            low=dataframe['low'][-length:],
            close=dataframe['close'][-length:],
            name='OHLC'
        )])

        fig.update_layout(xaxis_rangeslider_visible=False)
        # fig.update_layout(height=700, width=1600)
        fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),  # hide weekends
            ]
        )
        return fig.show()

