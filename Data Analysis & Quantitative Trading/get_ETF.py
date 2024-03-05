"""
1.台灣證卷交易所網站:https://www.twse.com.tw/zh/trading/historical/mi-index.html
我要抓每天ETF的資料 https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20240305&type=0099P&response=csv

2.
3.做ppt
"""

#https://www.wantgoo.com/stock/etf/ranking/volume
#https://tw.stock.yahoo.com/tw-etf/volume


import pandas as pd
import requests
url = 'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20240305&type=0099P&response=csv'
res = requests.get(url)
data = res.text
for d in data[0:500].split('\n'):
    print(d)
s_data = data.split('\n')
s_data[-100]
row = s_data[-100]
row.split(',')
