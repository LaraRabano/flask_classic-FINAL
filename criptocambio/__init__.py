from flask import Flask

FICHERO = "balance/data/movimientos.csv"

app = Flask(__name__)

APIKEY = "E1608E4F-F1D1-4449-B8A4-513461E57ECD"

MONEDAS = ("EUR - Euro",
           "ETH - Ethereum",
           "BNB - Binance coin",
           "LUNA - Terra",
           "SOL - Solana",
           "BTC - Bitcoin",
           "BCH - "Bitcoin Cash",
           "LINK - "Chainlink",
           "ATOM - "Cosmos"
           "USDT - Tether",)
