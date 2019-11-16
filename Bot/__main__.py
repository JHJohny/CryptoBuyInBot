from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance
from apscheduler.schedulers.blocking import BlockingScheduler

schedule = BlockingScheduler()

BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""
binance_client = Binance(BINANCE_API_KEY, BINANCE_API_SECRET)

bot_one = BotOne(exchange_client=binance_client, scheduler=schedule)

schedule.add_job(bot_one.check_for_opportunities, "interval", seconds=15)
schedule.start()