# -*- coding: utf-8 -*-
import python_bitbankcc
import requests
import json
import cgi
import time


base_url = "https://api.bitflyer.jp/v1/"

class bF_public(object):
    def __init__(self):
        pass

    def get(self,what,query=None):
        try :
            return json.loads(requests.get(base_url + what, params=query).text)
        except Exception as e:
            print(e)

api = bF_public()

#クエリパラメータを指定
query = {"product_code":"BTC_JPY"}

    #Tickerを取得
res= api.get("ticker",query)
    
    #表示
#print("[Bitflyer]現在のBTC/JPY BID : " + str(int(res["best_bid"])))
    
sbticker = 0 
pub = python_bitbankcc.public()   
while 1 < 3:
    time.sleep(1)
    bticker = pub.get_ticker("btc_jpy")
    if bticker["last"] != sbticker:
        print(str(bticker['timestamp'])+" [BitBank]現在のBTC/JPY BID : "+bticker["last"]+" JPY")
        sbticker = bticker["last"]
        

#btc_jpy, xrp_jpy, ltc_btc, eth_btc, mona_jpy, mona_btc, bcc_jpy, bcc_btc
     
#取得したティッカー情報を表示
#print("BitC---------------------------------------")
#print('現在の売り注文の最安値:' + bticker['sell'])
#print('現在の買い注文の最高値:' + bticker['buy'])
#print('過去24時間の最高値取引価格:' + bticker['high'])
#print('過去24時間の最安値取引価格:' + bticker['low'])
#print('最新取引価格:' + bticker['last'])
#print('過去24時間の出来高:' + bticker['vol'])
#print('タイムスタンプ(UnixTime):' + str(bticker['timestamp']))
