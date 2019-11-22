
"""Start menu
Start menu is guide for user to 'configure' bot - choose which bot user want to use, what exchange, APIs,
how much he wants to invest"""

def choose_bot():
    print("Select which bot you want to use")
    print("1.    Bot one (default)")
    print("More bots commint soon \n ...")
    def ask_for_input():
        users_input = input("Your choice ")
        if users_input == '1' or users_input == '':
            pass
        else:
            print("Sorry try again")
            ask_for_input()

def choose_exchange():
    print("Choose exchange for bot")
    print("1.    Binance (default)")
    print("More exchanges coming soon \n ...")
    def ask_for_input():
        users_input = input("Your choice ")
        if users_input == 1 or users_input == "":
            pass
        else:
            print("Sorry try again")
            ask_for_input()

def choose_invest_amount():
    print("How much you would like to invest")
    def ask_for_input():
        users_input = input("Enter amount")
        if users_input.isdigit():
            pass
        else:
            print("Sorry try again")
            ask_for_input()

