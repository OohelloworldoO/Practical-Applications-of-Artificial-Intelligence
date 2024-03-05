https://ithelp.ithome.com.tw/articles/10238573
https://ithelp.ithome.com.tw/m/articles/10269928
https://www.peteryangblog.com/posts/python-data-collecting-stock-price
https://hackmd.io/@s02260441/HJcMcnds8

網頁的基本組成: HTML + CSS + JavaScript
HTML: 主要為定義網頁的內容、結構。
CSS: 主要為設定顯示的風格 Style
JS: 行為...
HTML 是階層式文件結構，由許多元素(Elements)組成
一個元素包含開始標籤、結束標籤、屬性及內容，例如: <Tag 屬性>內容</Tag> 。

| 標籤名稱 |       用途       |
| :------: | :--------------: |
|    h     |       標題       |
|    p     |       段落       |
|  table   |       表格       |
|    td    |  表格內的 cell   |
|    br    | 換行(無結束標籤) |
|   href   |      超連結      |

| 屬性名稱 |        用途         |
| :------: | :-----------------: |
|  class   | 標籤的類別(可重複)  |
|    id    | 標籤的 id(不可重複) |
|  title   |   標籤的顯示資訊    |
|  style   |     標籤的樣式      |
| data-\*  |   自行定義的屬性    |
|   href   |       超連結        |

擷取網頁必要知識
在 HTTP 協定中，定義了多種不同的 method 做為服務的請求方法，近年來由於行動裝置的普及化，越來越多的產品及網站都提供了 WebAPI 服務，既然我們要擷取網頁內容，就必須知道對 HTTP 請求方式。
在 HTTP 1.1 的版本中定義了八種 Method (方法)，如下所示：
OPTIONS
GET
HEAD
POST
PUT
DELETE
TRACE
CONNECT
