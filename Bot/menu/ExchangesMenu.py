from Bot.BinanceAPI import API
"""Each exchange will have different kind of requirements, so for each one will have different menu"""


def get_binance_params():
    api_key = input("Insert your API key (Default from notes):   ")
    api_key_secret = input("Insert your API key secret (Default from notes):   ")

    if api_key == "":
        api_key = API.BINANCE_API_KEY

    if api_key_secret == "":
        api_key_secret = API.BINANCE_API_SECRET

    return {"api_key": api_key,
            "api_key_secret": api_key_secret}
