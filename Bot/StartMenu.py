
"""Start menu
Start menu is guide for user to 'configure' bot - choose which bot user want to use, what exchange, APIs,
how much he wants to invest"""

#choosing bot
def step_one():
    print("Select which bot you want to use")
    print("Bot one (default)")
    print("More bots commint soon \n ...")
    def ask_for_input():
        users_input = input("Your choice ")
        if users_input == '1' or users_input == '':
            pass
        else:
            print("Sorry try again")
            ask_for_input()

    ask_for_input()

step_one()