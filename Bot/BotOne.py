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
        """Checks for opportunity to make profit - every bot has different strategy"""

        #Get candle for each crypto
        cryptos_candles = {}
        for crypto_symbol in self.__list_of_cryptos:
            cryptos_candles[crypto_symbol] = self.exchange_client.get_current_minute_candle(crypto_symbol)

        #list trought all candles and look for opportunity
        for crypto in cryptos_candles:
            candle = cryptos_candles[crypto]
            if candle["change"] > self.min_pump:
                print(f"PUMP FOUND! {crypto}")
                pump = candle["change"]
                for crypto in cryptos_candles:
                    candle = cryptos_candles[crypto]
                    if (candle["change"] - pump) > self.min_opportunity:
                        print(f"OPPORTUNITY FOUND! {crypto}")
                    break
                break
                #TODO - send SMS, BUY in, pause a scheduler
            else:
                print(f"Nothing interesting for this crypto - {crypto} change only {candle['change']}")

    def __opportunity_found(self):
        """Call when one crypto didn't pump yet - so we can buy before it pumps and sell it at top"""
