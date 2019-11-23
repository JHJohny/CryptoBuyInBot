from abc import ABC, abstractmethod

class Bot(ABC):
    @abstractmethod
    def check_for_opportunities(self):
        pass

    @abstractmethod
    def start(self):
        pass
