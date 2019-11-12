from Bot.ExchangeBase import Exchange
from binance.client import Client

class Binance(Exchange):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(self.api_key, self.api_secret)

    def get_current_minute_candle(self, symbol):
        last_minute_candle = next(
            self.client.get_historical_klines_generator(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE,
                                                        start_str="1 minute ago UTC"))
        return {"open": float(last_minute_candle[1]),
                "high": float(last_minute_candle[2]),
                "low": float(last_minute_candle[3]),
                "close": float(last_minute_candle[4])}
