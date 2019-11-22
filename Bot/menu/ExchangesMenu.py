
"""Each exchange will have different kind of requirements, so for each one will have different menu"""

def binance_menu():
    api_key = input("Insert your API key")
    api_key_secret = input("Insert your API key secret")

    return {"api_key": api_key,
            "api_key_secret": api_key_secret}
