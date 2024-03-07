import pandas as pd
import matplotlib
import mplfinance as mpf 
# 導入pandas、matplotlib、mplfinance模組，將mplfinance模組縮寫為mpf
# 這邊要導入matplotlib的原因是因為mplfinance繪圖時需要調用mptplotlib模組 mplfinance是基於matplotlib開發的

target_stock = input('請輸入你要查詢的ETF: ')

#讀取目標股票csv檔的位置
filename =f'Data Analysis & Quantitative Trading/ETF_excel/{target_stock}.csv'
df = pd.read_csv(filename, parse_dates=True, index_col=1) 

#這裡針對資料表做一下修正，因為交易量(Turnover)在mplfinance中須被改為Volume才能被認出來
df.rename(columns={'Turnover':'Volume'}, inplace = True) 


#針對線圖的外觀微調 將上漲設定為紅色 下跌設定為綠色
my_color = mpf.make_marketcolors(up='r', down='g', inherit=True, edge='inherit', wick='inherit', volume='inherit')
#接著把自訂的marketcolors放到自訂的style中，而這個改動是基於預設的yahoo外觀
my_style  = mpf.make_mpf_style(marketcolors=my_color, figcolor='(0.82, 0.83, 0.85)', gridcolor='(0.82, 0.83, 0.85)')


#設定可變參數kwargs，並在變數中填上繪圖時會用到的設定值
kwargs = dict(type='candle', mav=(5,20,60), volume=True, figratio=(10,8), figscale=0.75, title=target_stock, style=my_style) 

#選擇df資料表為資料來源，帶入kwargs參數，畫出目標股票的走勢圖
mpf.plot(df,**kwargs)
