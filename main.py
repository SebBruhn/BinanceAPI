import logging
from data_collector import collect_all
from exchanges.binance import BinanceClient
#from coinbase.wallet.client import CoinbaseClient  (Haven't made)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

#logger.info("This is an info log")

#logger.debug("This is a debug log")

if __name__ == "__main__":

    mode = input("Choose the program mode (data/ backtest / optimize): ").lower()

    while True:
        exchange = input("Choose an exchange: ").lower()
        if exchange in ["Kraken", "binance"]:
            break
    
    if exchange == "binance":
        client = BinanceClient(True)
    #elif exchange == "bin":
        #client = binClient()
        #print(client.symbols)

    while True:
        symbol = input("Choose a symbol: ").upper()
        if symbol in client.symbols:
            break
    

    if mode == "data":
        collect_all(client, exchange, symbol)

    #client = BinanceClient(True)
    #print(client.get_historical_data("BTCUSDT"))

