#requests module用來下載網頁上的資料 透過http請求網頁伺服器下載指定的資料

import requests
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
if html.status_code == requests.codes.ok:
    print(html.text)