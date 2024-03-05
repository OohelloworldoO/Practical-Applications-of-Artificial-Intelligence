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

複習一下:

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
