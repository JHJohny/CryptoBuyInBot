from Bot.BotOne import BotOne
from Bot.BinanceExchange import Binance
from Bot.menu.ExchangesMenu import get_binance_params
from Bot.menu.ASCI import ASCI

"""Start menu
Start menu is guide for user to 'configure' bot - choose which bot user want to use, what exchange, APIs,
how much he wants to invest"""

def insert_fancy_lines(func):
    def insert():
        print(f"\n \n{ASCI.random_fancy_line}")
        return func()
    return insert

@insert_fancy_lines
def choose_exchange():
    print("Select exchange - \n"
          "1.  Binance\n"
          "2.  Comming soon\n"
          "\n")
    def ask_for_input():
        users_input = input("Your choice:   ")
        if users_input == "1" or users_input == "":
            api_params = get_binance_params()
            return Binance(api_params["api_key"], api_params["api_key_secret"])
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

@insert_fancy_lines
def choose_invest_amount():
    print("Invest amount\n"
          "Type how much you would like to invest\n"
          "\n")
    def ask_for_input():
        users_input = input("Enter amount:   ")
        if users_input.isdigit():
            return int(users_input)
        elif users_input == "":
            return 40
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

@insert_fancy_lines
def choose_bot():
    print("Select bot - \n"
          "1.    Bot one (default) Bot one detect pump in one crypto and will try to buy other cryptos as long they are still in low price\n"
          "2.    Comming soon\n"
          "\n")

    def ask_for_input():
        users_input = input("Your choice:   ")
        if users_input == '1' or users_input == '':
            return BotOne(exchange_client=choose_exchange(), buy_in_sum=choose_invest_amount())
        else:
            print("Sorry try again")
            return ask_for_input()

    return ask_for_input()

def main():
    print(ASCI.random_logo)
    bot = choose_bot()
    bot.start()

if __name__ == "__main__":
    main()
