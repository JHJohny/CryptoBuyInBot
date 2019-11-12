from abc import abstractmethod

class Exchange:

    @abstractmethod
    def get_current_minute_candle(self, symbol):
        """Takes keyword of cryptocurrency and returns dict of - Open, High, Low, Close values"""
        pass
