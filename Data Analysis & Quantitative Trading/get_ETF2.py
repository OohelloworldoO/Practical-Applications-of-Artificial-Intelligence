"""
需要twstock 而twstock需要lxml

"""
import twstock
import pandas as pd

target_stock = input('請輸入你要查詢的ETF: ')#股票代號變數

print('loading...')
#target_stock = '0050'  
stock = twstock.Stock(target_stock)  #告訴twstock我們要查詢的股票
target_price = stock.fetch_from(2020, 5)  #取用2020/05至今每天的交易資料

 #幫收集到的資料設定表頭
name_attribute = [
    'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
    'Transcation'
] 

#將twstock抓到的清單轉成Data Frame格式的資料表
df = pd.DataFrame(columns=name_attribute, data=target_price)



#指定Data Frame轉存csv檔案的檔名與路徑
#df.to_csv(target_stock+'.csv') 
filename = f'Data Analysis & Quantitative Trading/ETF_excel/{target_stock}.csv'

#將Data Frame轉存為csv檔案
df.to_csv(filename)

print('已儲存至指定資料夾')