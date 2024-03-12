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
import re
url = 'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20240305&type=0099P&response=csv'
res = requests.get(url)

# data的type是string
data = res.text

"""
透過Excel可以看到每筆資料的證卷代號前面有'=' 而每筆資料的matrix長度是16 
而台灣證卷交易所的每頁資料是10筆 共15頁+8筆 = 2528
而前面的header長度是182
包含標點符號
"""

for d in re.split("[=\r\n]",data):
   print(d)
    
"""
經過split()處理後 data type是list 可以透過index[]查詢 第一筆ETF資料從7開始 因為每個資料會空格兩行
那split無法達到我需要的效果 因為這樣太浪費空間
"""
#s_data = re.split("[=\r\n]",data)
s_data = re.sub(' = \r \n , \n',data)
#print(s_data)#檢查用
#print(len(s_data)) #查看list大小 20436

