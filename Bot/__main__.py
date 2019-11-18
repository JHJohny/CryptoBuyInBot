from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance
from Bot.BinanceAPI import API
from apscheduler.schedulers.blocking import BlockingScheduler

schedule = BlockingScheduler()

binance_client = Binance(API.BINANCE_API_KEY, API.BINANCE_API_SECRET)

bot_one = BotOne(exchange_client=binance_client, scheduler=schedule, buy_in_sum=40)

schedule.add_job(bot_one.check_for_opportunities, "interval", seconds=15)
schedule.start()
