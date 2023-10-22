#!/usr/bin/env python3
''' 
Flask server for coingecko app
Diego Pineda
Week2 Python Flask Server project
'''

from flask import Flask
from flask import render_template
import crypto_coingecko2 as crypto_coingecko

app = Flask(__name__)

@app.route("/")
def index():
    market_data = crypto_coingecko.get_marketdata()
    current_utctime = crypto_coingecko.get_utctime()
    return render_template("main.html", current_utctime=current_utctime, market_data=market_data)

@app.route("/coinslist")
def coinslist():
    #market_data = crypto_coingecko.get_marketdata()
    coins_list = crypto_coingecko.get_coinslist()
    current_utctime = crypto_coingecko.get_utctime()
    return render_template("coinslist.html", coins_list=coins_list, current_utctime=current_utctime)

@app.route("/<coin>")
def coindata(coin: str):
    coin_data = crypto_coingecko.get_coindata(coin)
    return render_template("getcoin.html", coin=coin, coin_data=coin_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
