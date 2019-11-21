from Bot.ExchangeBase import Exchange
from binance.enums import *
from binance.client import Client
import time

class Binance(Exchange):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(self.api_key, self.api_secret)

    def get_current_minute_candle(self, symbol):
        """Takes symbol of market - example BTCUSDT and returns current minute candle dictionary"""
        last_minute_candle = next(
            self.client.get_historical_klines_generator(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE,
                                                        start_str="1 minute ago UTC"))

        candle = {"open": float(last_minute_candle[1]),
                "high": float(last_minute_candle[2]),
                "low": float(last_minute_candle[3]),
                "close": float(last_minute_candle[4])} #close is current status - current minute is not closed yet

        change = ((100 / candle["open"]) * candle["close"]) - 100
        candle["change"] = change

        return candle

    def create_buy_order(self, amount, crypto, timeout=10):
        order = self.client.order_market_buy(symbol=crypto, quantity=amount)
        order = self.wait_till_order_is_filled(order["orderId"])

        #Nah block below looks weird, think about refactoring
        completed_order = {
            "symbol" : crypto,
            "amount" : self.__amount_after_comission(order),
            "price" : order["fills"][0]["price"] #TODO - make average of price
        }

        return completed_order

    def set_stop_loss(self, *, crypto, amount, stop_loss_price):
        order = self.client.create_order(symbol=crypto,
                                 side="SELL",
                                 type="STOP_LOSS",
                                 timeInForce="GTC",
                                 quantity=amount,
                                 price=stop_loss_price)
        return order

    def set_stop_profit(self, *, crypto, amount, profit_price):
        order = self.client.create_order(symbol=crypto,
                                 side="SELL",
                                 type="TAKE_PROFIT",
                                 timeInForce="GTC",
                                 quantity=amount,
                                 price=profit_price)

        return order

    def wait_till_order_is_filled(self, timeout=15, *orderIds):
        """Wait till order is completed or timeouted - if it's timeouted cancel order and return order
        If multiple orders are inserted, stop wait when first one got filled or timeouted"""
        elapsed_time = 0
        while elapsed_time < timeout:
            for orderId in orderIds:
                order_status = self.client.get_order(orderId=orderId)["status"]
                if order_status != "FILLED":
                    time.sleep(0) if timeout is None else time.sleep(1), elapsed_time.__add__(1)
                else:
                    return self.client.get_order(orderId=orderId)
        else:
            for orderId in orderIds:
                order = self.client.get_order(orderId=orderId)
                self.client.cancel_order(symbol=order["symbol"], orderId=orderId)
                order = self.client.get_order(orderId=orderId)
                return order

    def __amount_after_comission(self, order):  # Will calculate final bought amount - comissions removed
        amount = 0
        comissions = 0
        for fill in order["fills"]:
            amount += float(fill["qty"])
            comissions += float(fill["commission"])

        return amount - comissions

