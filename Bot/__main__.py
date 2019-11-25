import sys
from Bot.menu.MenuInterface import start_menu
from Bot.menu.CommandLineInterface import start_cli


if __name__ == "__main__":
    print("Main is running")
    if len(sys.argv) > 1: #2 ways how to start bot
        start_cli()
    else:
        start_menu()
