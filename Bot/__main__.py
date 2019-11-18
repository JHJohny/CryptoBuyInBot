from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance
from Bot.BinanceAPI import API
from apscheduler.schedulers.blocking import BlockingScheduler

schedule = BlockingScheduler()

order = {'symbol': 'ETHUSDT', 'orderId': 499862219, 'orderListId': -1, 'clientOrderId': 'BSMRCuML18styKVHQSoNIk', 'transactTime': 1574025252972, 'price': '0.00000000', 'origQty': '0.10000000', 'executedQty': '0.10000000', 'cummulativeQuoteQty': '18.43800000', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '184.38000000', 'qty': '0.00080000', 'commission': '0.00000550', 'commissionAsset': 'BNB', 'tradeId': 105435766}, {'price': '184.38000000', 'qty': '0.09920000', 'commission': '0.00009920', 'commissionAsset': 'ETH', 'tradeId': 105435767}]}
binance_client = Binance(API.BINANCE_API_KEY, API.BINANCE_API_SECRET)

# print(binance_client.client.get_order(symbol="BNBUSDT", orderId=284246743))
#
# bot_one = BotOne(exchange_client=binance_client, scheduler=schedule, buy_in_sum=40)
#
# schedule.add_job(bot_one.check_for_opportunities, "interval", seconds=15)
# schedule.start()
