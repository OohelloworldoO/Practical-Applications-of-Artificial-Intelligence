# 需要twstock 而twstock需要lxml
import twstock
import pandas as pd # 將list轉換成 Data Frame格式用

target_stock = input('請輸入你要查詢的ETF: ')
year= int(input('請輸入查詢起始年分: '))
month= int(input('月分: '))
print('Loading...')
# target_stock = '0050'
stock = twstock.Stock(target_stock)
target_price = stock.fetch_from(year,month)

# 類別有: Date, capacity, turnover, open, high, low, close, change, transaction
#print(target_price) #印出全部資料


 # 幫收集到的資料設定表頭
name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transcation']

# 將twstock抓到的清單轉成Data Frame格式的資料表
df = pd.DataFrame(columns = name_attribute, data = target_price)
#print(df) #檢查用

# 指定Data Frame轉存csv檔案的檔名與路徑
#df.to_csv(target_stock+'.csv') 
filename = f'Data Analysis/ETF_excel/{target_stock}.csv'

# 將Data Frame轉存為csv檔案
#df.to_csv(filename)
def Data_Frm(name):
    df.to_csv(name)
    return print("已存入指定資料夾")

data_Save = Data_Frm(filename)

"""
#這樣也可以獲取指定股票 指定年份~今日的所有訊息 不過我認為使用twstock可以幫我省略很多我不需要的資訊
import yfinance as yf
df=yf.Ticker("006208.TW").history(period="3y")
df=df.filter("Close") # 過濾需要的Topic
"""




