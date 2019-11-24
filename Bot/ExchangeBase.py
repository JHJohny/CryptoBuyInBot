from abc import ABC, abstractmethod


class Exchange(ABC):

    @abstractmethod
    def get_current_minute_candle(self, symbol):
        """Takes keyword of cryptocurrency and returns dict of - Open, High, Low, Close values"""
        pass

    @abstractmethod
    def create_buy_order(self):
        pass

    @abstractmethod
    def set_stop_loss(self):
        pass

    @abstractmethod
    def set_stop_profit(self):
        pass
