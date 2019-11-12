from abc import abstractmethod


class Exchange:
        def __init__(self, api_key):
            self.api_key = api_key

        @abstractmethod
        def get_two_min_history(self):
            pass
