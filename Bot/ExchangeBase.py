from abc import ABC, abstractmethod

class Exchange(ABC):

    @abstractmethod
    def get_current_minute_candle(self, symbol):
        """Takes keyword of cryptocurrency and returns dict of - Open, High, Low, Close values"""
        pass

    @abstractmethod
    def buy_in(self):
        pass

    @abstractmethod
    def sell_position(self):
        pass

    #TODO - add abtract function to set autosell