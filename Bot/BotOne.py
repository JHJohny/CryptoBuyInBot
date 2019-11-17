from Bot.BotBase import Bot
import time

"""Bot One - logic

Bot one is simplest concept. Bot one checks prices of main crypto currencies for rapid/move to upside.
If bot detect massive movement on one crypto, will try to buy other currencies as long they are on low price.
Whole idea is - when bitcoin moves up, we expect all crypto moves up as well.
"""

class BotOne(Bot):
    __list_of_cryptos = ["BTCUSDT", "ETHUSDT", "BCHABCUSDT", "LTCUSDT", "XRPUSDT"]

    def __init__(self, *, exchange_client, scheduler, buy_in_amount, list_of_cryptos=__list_of_cryptos, min_pump=7, min_oppor=5):
        self.exchange_client = exchange_client
        self.scheduler = scheduler
        self.buy_in_amount = buy_in_amount
        self.__list_of_cryptos = list_of_cryptos
        self.min_pump = min_pump # % that crypto must reach, to consider it as pump
        self.min_opportunity = min_oppor # % difference between already pumping crypto and not yet pumping crypto

    def check_for_opportunities(self):
        """Checks for opportunity to make profit - every bot has different strategy
        pump - when one crypto is above x %
        opportunity - when pump is found and found is also crypto that isn't pumped yet - that is opportunity to buy in"""

        #record changes for each crypto
        changes = {}
        for crypto in self.__list_of_cryptos:
            changes[crypto] = self.exchange_client.get_current_minute_change(crypto)

        #actual checking for pump and opportunities
        for crypto, change in changes.items(): #looking for pump
            if change > self.min_pump:
                print(f"Pump found! in {crypto}, change - {change}")

                pump = change
                for crypto, change in changes.items(): #looking for opportunity
                    if (pump - change) > self.min_opportunity:
                        print(f"Opportunity FOUND! {crypto}")
                        self.__opportunity_found()
                        break
                break

        print("Nothing interesting found keep looking")

    def __opportunity_found(self):
        """Call when one crypto didn't pump yet - so we can buy before it pumps and sell it at top"""
        self.scheduler.pause() #Pause scheduler for looking opportunity - we found already one
        self.exchange_client.buy_in(self.buy_in_amount)
        #TODO - send a SMS - via multi threading or multi processing