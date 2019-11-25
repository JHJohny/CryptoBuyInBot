import argparse
from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance

def start_cli():
    parser = argparse.ArgumentParser(prog="CryptoBot",
                                     usage="%(prog)s -b BotOne -e Binance -k *YourKey -s *YourSecret -a 100 \n"
                                           "Or use non command line interface, without any parameters - $ %(prog)s",
                                     description="Crypto bot is collection of bots for trading on multiple exchanges",
                                     allow_abbrev=False)

    parser.version = "0.1"
    parser.add_argument("-v", "--Version", action="version", help="Display version of bot.")
    parser.add_argument("-b", "--Bot", type=str, choices=["BotOne"], required=True, metavar="", help="Select one bot from collection")
    parser.add_argument("-e", "--Exchange", type=str, metavar="", choices=["Binance"], required=True, help="Select exchange that you want trade on")
    parser.add_argument("-k", "--Key", required=True, metavar="", help="Insert your exchange API")
    parser.add_argument("-a", "--Amount", type=int, required=True, metavar="", help="Insert how much you want trade with")
    parser.add_argument("-s", "--Secret", required=False, metavar="", help="API Key Secret if you want to trade with Binance")
    parser.add_argument("-i", "--Interval", type=int, required=False, choices=range(1, 59), metavar="", help="Custom interval how often check market")
    parser.add_argument("-d", "--Debug", type=int, required=False, choices=[1, 2, 3], metavar="", help="Select level of console debug \n"
                                                                                                       "1. Lowest (recommended) 3. Highest")
    #TODO - add parameter for custom cryptos
    args = parser.parse_args()

    print(args.Key)

#TODO - construc a bot

if __name__ == "__main__":
    start_cli()


def _start_bot(args):
    if args.Bot == "BotOne":
        if args.Secret == "":
            raise Exception("Missing secret argument, if you want to use Binance, "
                            "you need insert API key secret as well. use -s or --Secret argument")
        else:
            exchange = Binance(api_key=args.Key, api_secret=args.Secret)
            bot = BotOne(exchange_client=exchange, buy_in_sum=args.Amount)
            bot.start()
