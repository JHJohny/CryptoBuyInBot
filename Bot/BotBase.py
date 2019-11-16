from abc import ABC, abstractmethod

class Bot(ABC):
    @abstractmethod
    def check_for_opotunities(self):
        pass

    @abstractmethod
    def buy_in(self):
        pass

    @abstractmethod
    def sell_position(self):
        pass
