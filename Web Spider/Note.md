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

[資料來源 1](https://pypi.org/project/requests/)
[資料來源 2](https://github.com/requests/requests)
[資料來源 3](http://docs.python-requests.org/en/master/user/quickstart/)
