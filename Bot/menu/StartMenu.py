from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance
from Bot.menu.ExchangesMenu import get_binance_params

"""Start menu
Start menu is guide for user to 'configure' bot - choose which bot user want to use, what exchange, APIs,
how much he wants to invest"""

def choose_exchange():
    print("Choose exchange for bot")
    print("1.    Binance (default)")
    print("More exchanges coming soon...")
    def ask_for_input():
        users_input = input("Your choice ")
        if users_input == "1" or users_input == "":
            api_params = get_binance_params()
            return Binance(api_params["api_key"], api_params["api_key_secret"])
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

def choose_invest_amount():
    print("How much you would like to invest, (40 default)")
    def ask_for_input():
        users_input = input("Enter amount")
        if users_input.isdigit():
            return int(users_input)
        elif users_input == "":
            return 40
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

def choose_bot():
    print("Select which bot you want to use")
    print("1.    Bot one (default)")
    print("More bots commint soon ...")
    def ask_for_input():
        users_input = input("Your choice")
        if users_input == '1' or users_input == '':
            return BotOne(exchange_client=choose_exchange(), buy_in_sum=choose_invest_amount())
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

def main():
    bot = choose_bot()
    bot.start()

if __name__ == "__main__":
    main()
