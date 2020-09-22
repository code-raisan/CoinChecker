# -*- coding: utf-8 -*-
from datetime import datetime
import requests
import json
import time

bitflyer_api = "https://api.bitflyer.jp/v1/ticker?product_code="
coincheck_api = "https://coincheck.com/api/ticker"
bitbank_api = "https://public.bitbank.cc/btc_jpy/ticker"

bitflyer_old = 0
coincheck_old = 0
bitbank_old = 0

while 1< 2:
    time.sleep(1)
    now_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    bitflyer_res = requests.get(bitflyer_api + "BTC_JPY")
    bitflyer = bitflyer_res.json()
    coincheck_res = requests.get(coincheck_api)
    coincheck = coincheck_res.json()
    bitbank_res = requests.get(bitbank_api)
    bitbank = bitbank_res.json()

    if bitflyer["ltp"] != bitflyer_old:
        print("[Bitflyer]  " + "¥ {:,.0f}".format(bitflyer["ltp"]) + "  " + now_date)
        bitflyer_old = bitflyer["ltp"]

    if coincheck["last"] != coincheck_old:
        print("[CoinCheck] " + "¥ {:,.0f}".format(coincheck["last"]) + "  " + now_date)
        coincheck_old = coincheck["last"] 

    if bitbank["data"]["last"] != bitbank_old:
        print("[BitBank]   " + "¥ {:,.0f}".format(int(bitbank["data"]["last"])) + "  " + now_date)
        bitbank_old = bitbank["data"]["last"]
