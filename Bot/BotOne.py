from Bot.BotBase import Bot
import datetime

"""Bot One - logic

Bot one is simplest concept. Bot one checks prices of main crypto currencies for rapid/move to upside.
If bot detect massive movement on one crypto, will try to buy other currencies as long they are on low price.
Whole idea is - when bitcoin moves up, we expect all crypto moves up as well.
"""

class BotOne(Bot):
    __list_of_cryptos = ["BTCUSDT", "ETHUSDT", "BCHABC", "LTCUSDT", "XRPUSDT"]

    def __init__(self, *, BotClient, scheduler, list_of_cryptos=__list_of_cryptos):
        self.BotClient = BotClient
        self.__list_of_cryptos = list_of_cryptos
        self.scheduler = scheduler

    def check_for_opotunities(self):
        print("Bot is checking for price ", datetime.datetime.now())
