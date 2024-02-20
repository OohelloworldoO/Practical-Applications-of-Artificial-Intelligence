# Tensorflow-Keras

## 建立Tensorflow的Anaconda虛擬環境  

### 1.建立&切換工作目錄  

<pre>
md \pythonwork
cd \pythonwork
</code></pre>

### 2.建立Anaconda虛擬環境  

<pre>
conda create --name tensorflow python=3.5 anaconda
</code></pre>
這邊我原本是照著書本上的使用cmd，但無法辨識"conda"的comand，所以我用anaconda prompt也能正常運行


|  comand   | 用途  |
|  :----:  | :----:  |
|  conda create  | 建立虛擬環境  |
| --name tensorflow  | 虛擬環境命名:tensorflow |
| python=3.5  | version |
| anaconda  | 建立虛擬環境時 也會同時安裝其他python軟件 |

安裝完成後:  

![註解1](/images/1.png "1")

啟動&關閉:  
書本上是教更新前的指令來退出tensorflow虛擬環境:
<pre>
deactivate tensorflow
</code></pre>


現在不需要在後面添加要退出的python name of envirement了，只需要輸入:
<pre>
conda deactivate
</code></pre>

![註解2](/images/2.png "2")


### 3.在Anaconda虛擬環境安裝Tensorflow & Keras  

<pre>
activate tensorflow
pip install tensorflow
pip install Keras
</code></pre>

我自己是出現這個問題:

![註解3](/images/3.png "3")

會遇到這個問題是因為安裝Anaconda的時候沒有新增[環境變數]
因此使用者必須手動加入
在[搜尋]列中輸入[環境變數]，點擊[編輯系統環境變數]  
路徑通常可以在「C:\Users\使用者名稱\anaconda3\Scripts」目錄底下可以找到  

[重啟]命令提示列，再次輸入[jupyter notebook]
會遇到新的問題：「ImportError: DLL load failed: 找不到指定的模組。」
要解決這個問題，得將相關模組的路徑也加入環境變數
這個路徑通常在「C:\Users\使用者名稱\anaconda3\Library\bin」，回去編輯環境變數，再次新增變數路徑。再次重啟就成功了