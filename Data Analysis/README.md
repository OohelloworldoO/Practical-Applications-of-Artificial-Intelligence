原本是照著老師上課用的 Spyder Launch 操作 但發現編譯的問題很多(像是可以輸出卻無法輸入) 加上不熟悉  
後來所以改成用我最熟悉的 vscode 操作 因為我以前寫 python 也是用 vscode 環境都已經弄好了 用 markdown 寫筆記也可以及時看到成效(不用 git push)

# 股票

## K 線

![註解1](./images/k線.png "k線")
[圖片來源網址](https://tw.stock.yahoo.com/news/%E4%BB%80%E9%BA%BC%E6%98%AFk%E7%B7%9Ak%E7%B7%9A%E6%80%8E%E9%BA%BC%E7%9C%8B-102019742.html)

K 線又稱作蠟燭線，一根蠟燭表示一天自開盤到收盤的價格表現 其中紅色代表上漲 綠色代表下跌(話說我一直以為綠色是上漲)  
而中間的蠟燭上下限標記開盤及收盤價格 K 線的上下橫線則為當日最高與最低價格

## 均線

均線紀錄了一段特定時間中股票持有成本的平均值 英文原名是 Moving Average(MA)
舉例來說，下表是某檔股票 5 日的收盤價格，將 5 日的價格加總除以 5 即為 5 日均價，以每一天為中心計算前後兩日加總的均價，就能連成一條 5 日價格均線了。

|   時間   | 價格  |
| :------: | :---: |
|   D-2    | 52.5  |
|   D-1    | 53.0  |
|    D     | 59.5  |
|   D+1    | 55.2  |
|   D+2    | 49.5  |
| 5 日均價 | 53.94 |

而隨著加總平均計算的天數不同 均線代表的意涵也不同 以下是常見的均線技術分析:

|  均線種類  |         說明         |              分析意義              |
| :--------: | :------------------: | :--------------------------------: |
|  5 日均線  | 周線，極短線操作指標 |     飆股跌破周線可能是出場時機     |
| 10 日均線  | 雙周線，短線操作指標 | 強勢股跌破雙周線可能會進入短期整理 |
| 20 日均線  |  月線，多頭操作指標  | 跌破月線可能會進入短期空頭修正格局 |
| 60 日均線  |  季線，中期操作指標  | 跌破季線可能會進入長期空頭修正格局 |
| 240 日均線 |  年線，長期操作指標  | 跌破年線可能會進入長期空頭修正格局 |

## 交易量

圖片下方的副圖表為每日的交易量 長條圖顏色對應當日的漲跌顯示

# 複習一下網頁組成

網頁的基本組成: HTML + CSS + JavaScript  
HTML: 主要為定義網頁的內容、結構  
CSS: 主要為設定顯示的風格 Style  
JS: 操作、動作(?)  
HTML 是階層式文件結構，由許多元素(Elements)組成  
一個元素包含開始標籤、結束標籤、屬性及內容，例如:

<pre>
<Tag 屬性>內容</Tag>
</code></pre>

| 標籤名稱 |       用途       | 屬性名稱 |        用途         |
| :------: | :--------------: | :------: | :-----------------: |
|    h     |       標題       |  class   | 標籤的類別(可重複)  |
|    p     |       段落       |    id    | 標籤的 id(不可重複) |
|  table   |       表格       |  title   |   標籤的顯示資訊    |
|    td    |  表格內的 cell   |  style   |     標籤的樣式      |
|    br    | 換行(無結束標籤) | data-\*  |   自行定義的屬性    |
|   href   |      超連結      |   href   |       超連結        |

在 HTTP 協定中，定義了多種不同的 method 做為服務的請求方法，近年來由於行動裝置的普及化，越來越多的產品及網站都提供了 WebAPI 服務，既然我們要擷取網頁內容，就必須知道對 HTTP 請求方式。

在 HTTP 1.1 的版本中定義了八種 Method (方法)，如下所示：

- OPTIONS
- GET
- HEAD
- POST
- PUT
- DELETE
- TRACE
- CONNECT

在 HTTP 2 的版本中定義了八種 Method (方法)，如下所示：
2015 年誕生了一個新的 HTTP 版本，稱為 HTTP/2。HTTP/2 解決了 HTTP/1.1 的創造者未曾預料的幾個問題。特別是，HTTP/2 比 HTTP/1.1 更快，更高效。HTTP/2 速度更快的一個表現是在載入過程中如何對內容進行優先順序排序。

## requests module 用來下載網頁上的資料 透過 http 請求網頁伺服器下載指定的資料

Get 請求即可直接下載
將 parameter 存在 r

<pre>
# 引入 requests 模組
import requests

# 使用 GET 方式下載普通網頁
r = requests.get('https://www.google.com.tw/')

# 伺服器回應的狀態碼 如果顯示200就代表沒問題
print(r.status_code)

# 也可以這樣檢查狀態碼是否 OK
if r.status_code == requests.codes.ok:
  print("OK")
</code></pre>

## 增加 URL 查詢 parameter

許多 GET 請求都會在 URL 中夾帶簡短的查詢 parameter(例如關鍵字)

<pre>
# 查詢參數
my_params = {'key1': 'value1', 'key2': 'value2'}

# 將查詢參數加入 GET 請求中
r = requests.get('http://httpbin.org/get', params = my_params)

# 觀察 URL
print(r.url)
</code></pre>

## 回應資料分析 從回應中取出各種我們需要的資料

<pre>

print(r.text) #列出文字

print(r.encoding) #列出編碼

print(r.status_code) #列出 HTTP 狀態碼

print(r.headers) #列出 HTTP Response Headers

print(r.headers['Content-Type']) #印出 Header 中的 Content-Type

</code></pre>

## 自訂請求 header

<pre>
# 自訂表頭 許多時候網站會擋掉 UA 是 python-request 的請求，因此我們很常需要自訂 Header
my_headers = {'user-agent': 'my-app/0.0.1'}

# 將自訂表頭加入 GET 請求中
r = requests.get('http://httpbin.org/get', headers = my_headers)
</code></pre>

##　解析 JSON 資料
如果取得的是 json 格式資料 requests 有內建解析函式

<pre>
r = requests.get('https://api.github.com/events')
r.json()
</code></pre>

## Timeout()

避免程式在維修中或故障的網站停留太久 或是用來檢查是否可存取時很方便

<pre>
requests.get('http://github.com', timeout=[SECOND])
</code></pre>

## 指定編碼

通常網站會使用 UTF-8 編碼 但若不是可用這個方法修改讀取編碼

<pre>
r.encoding = 'ISO-8859-1'
</code></pre>

## 帳戶密碼登入

若遇到需要帳密登入後才能看的網頁(HTTP 基本認證) 可以使用 auth 參數指定帳密:

<pre>
# 需要帳號登入的網頁
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
</code></pre>

## POST 請求

POST 請求也是常用的 HTTP 請求 只要是網頁中有讓 user 填入資料的表單 大部分都會需要 POST 請求來處理

<pre>
# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}

# 將資料加入 POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
</code></pre>

若有遇到重複鍵值（key）的 HTML 表單欄位，可以這樣處理：

<pre>
# 具有重複鍵值的資料
my_data = (('key1', 'value1'), ('key1', 'value2'))

# 將資料加入 POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
</code></pre>

## Upload

若要上傳檔案也可使用 POST 請求處理

<pre>
# 要上傳的檔案
my_files = {'my_filename': open('my_file.docx', 'rb')}

# 將檔案加入 POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)
</code></pre>

## Cookie

如果 server 回傳的 html 資料中含有 cookies requests 也可以取出 cookies 資料

<pre>
# 含有 cookie 的內容
r = requests.get("http://my.server.com/has/cookies")

# 取出 cookie
print(r.cookies['my_cookie_name'])
</code></pre>

若要將自己設定的 cookis 放進 GET 請求中給 server:

<pre>
# 設定 cookie
my_cookies = dict(my_cookie_name='G. T. Wang')

# 將 cookie 加入 GET 請求
r = requests.get("http://httpbin.org/cookies", cookies = my_cookies)
</code></pre>

## 修改 Cookie

<pre>
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text
</code></pre>

# python 補充新版本內容

## f-string

f-string 是 Python 3.6 加入的字串格式化功能 也是現在比較推薦的格式化方法
操作方式為「f{變數名稱或運算式}」( 開頭可以使用 f 或 F ) 輸出結果會將變數或運算式的內容放入指定的位置
下方的程式執行後 會將變數 a 和 b 的內容 放入 c 的字串裡

<pre>
a = 'world'
b = 'oxxo'
c = f'hello {a}, I am {b}'
print(c)   # hello world, I am oxxo
</code></pre>

可以透過字串格式化的方式 實作補零的效果

<pre>
for i in range(1,101):
  print(f'{i:03d}',end=' , ')
</code></pre>

輸出:

'''
001 , 002 , 003 , 004 , 005 , 006 , 007 , 008 , 009 , 010 ,
011 , 012 , 013 , 014 , 015 , 016 , 017 , 018 , 019 , 020 ,
021 , 022 , 023 , 024 , 025 , 026 , 027 , 028 , 029 , 030 ,
031 , 032 , 033 , 034 , 035 , 036 , 037 , 038 , 039 , 040 ,
041 , 042 , 043 , 044 , 045 , 046 , 047 , 048 , 049 , 050 ,
051 , 052 , 053 , 054 , 055 , 056 , 057 , 058 , 059 , 060 ,
061 , 062 , 063 , 064 , 065 , 066 , 067 , 068 , 069 , 070 ,
071 , 072 , 073 , 074 , 075 , 076 , 077 , 078 , 079 , 080 ,
081 , 082 , 083 , 084 , 085 , 086 , 087 , 088 , 089 , 090 ,
091 , 092 , 093 , 094 , 095 , 096 , 097 , 098 , 099 , 100 ,
'''

# 參考資料:

[1. 爬蟲相關](https://pypi.org/project/requests/)  
[2. 爬蟲相關](https://github.com/requests/requests)  
[3. 爬蟲相關](http://docs.python-requests.org/en/master/user/quickstart/)
[4. 爬蟲相關](https://ithelp.ithome.com.tw/articles/10238573)  
[5. 爬蟲相關](https://ithelp.ithome.com.tw/m/articles/10269928)  
[6. 爬蟲相關](https://www.peteryangblog.com/posts/python-data-collecting-stock-price)  
[7. 爬蟲相關](https://www.youtube.com/watch?v=1PHp1prsxIM)  
[8. Fix module pandas](https://www.statology.org/module-pandas-has-no-attribute-dataframe/)  
[9.](https://hackmd.io/@s02260441/HJcMcnds8)
[10.](https://hackmd.io/v7m8LMfzQHu1y_dQNuXwbQ)  
[11. mplfinance 相關](https://blog.csdn.net/Shepherdppz/article/details/117575286)  
[12. mplfinance 相關](https://www.grenade.tw/blog/how-to-use-the-python-financial-analysis-visualization-module-mplfinance/)  
[13. mplfinance 相關](https://blog.csdn.net/ooobenooo/article/details/107754092)  
[14. python 格式化](https://steam.oxxostudio.tw/category/python/basic/format.html)  
[15. 量化分析 mplfinance 問題](https://github.com/matplotlib/mplfinance/issues/89)  
[16. 量化分析 mplfinance 問題](https://cloud.tencent.com/developer/ask/sof/108763483)  
[17. 量化分析 mplfinance 問題](https://stackoverflow.com/questions/67225879/how-can-i-deal-with-expect-data-index-as-datetimeindex)  
[18. 量化分析 mplfinance 問題](https://aitechtogether.com/python/132185.html)  
[19. twstock moduel](https://twstock.readthedocs.io/zh-tw/latest/reference/stock.html)  
[20. 資料分析 & 機器學習](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-2%E8%AC%9B-%E5%A6%82%E4%BD%95%E7%8D%B2%E5%8F%96%E8%B3%87%E6%96%99-google-map-api-beb7c88dc4e3)
