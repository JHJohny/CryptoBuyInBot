from Bot.BotBase import Bot
import time

"""Bot One - logic

Bot one is simplest concept. Bot one checks prices of main crypto currencies for rapid/move to upside.
If bot detect massive movement on one crypto, will try to buy other currencies as long they are on low price.
Whole idea is - when bitcoin moves up, we expect all crypto moves up as well.
"""

class BotOne(Bot):
    __list_of_cryptos = ["BTCUSDT", "ETHUSDT", "BCHABCUSDT", "LTCUSDT", "XRPUSDT"]

    def __init__(self, *, exchange_client, scheduler, buy_in_amount, list_of_cryptos=__list_of_cryptos, min_pump=7):
        self.exchange_client = exchange_client
        self.scheduler = scheduler
        self.buy_in_amount = buy_in_amount
        self.__list_of_cryptos = list_of_cryptos
        self.min_pump = min_pump

    def check_for_opportunities(self):
        """Checks for opportunity to make profit - every bot has different strategy"""

        print("checking for opportunities")

        #Get candle for each crypto
        cryptos_candles = {}
        for crypto_symbol in self.__list_of_cryptos:
            cryptos_candles[crypto_symbol] = self.exchange_client.get_current_minute_candle(crypto_symbol)

        #list trought all candles and opportunity
        for crypto in cryptos_candles:
            candle = cryptos_candles[crypto]
            if candle["change"] > self.min_pump:
                print("OPPORTUNITY to profit!")
                #TODO - send SMS
                self.scheduler.pause() #Pause till we will find another opportunity after we sell profit from current opportunity
                self.buy_in(crypto, self.buy_in_amount)
            else:
                print(f"Nothing interesting for this crypto - {crypto} change only {candle['change']}")

    def __buy_in(self, crypto, amount):
        #TODO - implementation for binance to buy in
        pass

    def __sell_position(self):
        #TODO - implemenation for binance to sell specific position
        pass