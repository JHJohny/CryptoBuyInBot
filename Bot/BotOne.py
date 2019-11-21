from Bot.BotBase import Bot
from utils.mathematics import get_x_percent_of_y
import time

"""Bot One - logic

Bot one is simplest concept. Bot one checks prices of main crypto currencies for rapid/move to upside.
If bot detect massive movement on one crypto, will try to buy other currencies as long they are on low price.
Whole idea is - when bitcoin moves up, we expect all crypto moves up as well.
"""

class BotOne(Bot):
    __list_of_cryptos = ["BTCUSDT", "ETHUSDT", "BCHABCUSDT", "LTCUSDT", "XRPUSDT"]

    def __init__(self, *, exchange_client, scheduler, buy_in_sum, list_of_cryptos=__list_of_cryptos, min_pump=4, min_oppor=3):
        self.exchange_client = exchange_client
        self.scheduler = scheduler
        self.buy_in_sum = buy_in_sum
        self.__list_of_cryptos = list_of_cryptos
        self.min_pump = min_pump # % that crypto must reach, to consider it as pump
        self.min_opportunity = min_oppor # % difference between already pumping crypto and not yet pumping crypto

    def check_for_opportunities(self):
        """Checks for opportunity to make profit - every bot has different strategy
        pump - when one crypto is above x %
        opportunity - when pump is found and found is also crypto that isn't pumped yet - that is opportunity to buy in"""

        #record candles for each crypto
        candles = {}
        for crypto in self.__list_of_cryptos:
            candles[crypto] = self.exchange_client.get_current_minute_candle(crypto)

        #actual checking for pump and opportunities
        for crypto, candle in candles.items(): #looking for pump
            if candle["change"] > self.min_pump:
                print(f"Pump found! in {crypto}, change - {candle['change']}")

                pump = candle["change"]
                for crypto, change in candles.items(): #looking for opportunity
                    if (pump - change) > self.min_opportunity:
                        print(f"Opportunity FOUND! {crypto}")
                        self.__opportunity_found(crypto, candle["close"])
                        break
                break
            else:
                print(f"Nothing special found in {crypto} , change only {candle['change']}")
        print(f"Not opportunities found")

    def __opportunity_found(self, crypto, crypto_price):
        """Call when one crypto didn't pump yet - so we can buy before it pumps and sell it with profit"""

        self.scheduler.pause() #Pause scheduler for looking opportunity - we found already one
        buy_order = self.exchange_client.create_buy_order(int(self.buy_in_sum / crypto_price), crypto)
        stop_loss_order = self.exchange_client.set_stop_loss(symbol=buy_order["symbol"],
                                                             amount=buy_order["amount"],
                                                             stop_loss_price=get_x_percent_of_y(x=97, y=buy_order["price"]))

        stop_profit_order = self.exchange_client.set_stop_profit(symbol=buy_order["symbol"],
                                                                 amount=buy_order["amount"],
                                                                 stop_loss_price=get_x_percent_of_y(x=103, y=buy_order["price"]))

        filled_order = self.exchange_client.wait_till_order_is_filled(stop_loss_order["orderId"], stop_profit_order["orderId"], timeout=None)
        print("ORDER COMPLETED - ", filled_order)
        time.sleep(300) #Wait, market can be stable right after big pumps
        self.scheduler.resume()

        #TODO - send a SMS - via multi threading or multi processing