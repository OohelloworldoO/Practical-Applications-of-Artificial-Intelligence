# What are the different between ML and DL?

釐清前對於 AI 我是毫無頭緒 甚至不知道從何開始學起  
所以在學習前 我想先搞懂 ML、DL 還有一些甚麼 NN、CNN、RNN...等等之間的關係  
還有像是 tensorflow、opencv、Bert 是做甚麼用的等等...

Deep Learning => Neural Network => Machine Learning => AI

![Artificial Intelligence](<./Machine%20Learning(ML)/images/Artificial%20Intelligence.png> "AI")

## Machine Learning

我們定義模型中的權重(weight) 並使用激活函數(Activation Function)來計算  
Classical Machine Learning 更依賴人類干預來學習 由我們來定義特徵的層次結構來理解資料輸入之間的差異 過程包括人工干預/人工監督 (human supervision)

### What is Activation Function?

在 NN 中 我們會發現 在每一層的 NN 輸出後都會使用一個函數(Sigmoid, Tanh, ReLU...)對結果進行運算 這個函數就是激活函數  
而 Activation Function 就是在幫助機器學習資料中的複雜模式  
激活函數分為 線性(如: f(x)=x ) /非線性激活函數(如: Sigmoid, Tanh, ReLU, LReLU, PReLU, Swish)

因為 NN 中的每個 Layer in/output 都是線性求和的過程 下一層的輸出只是承接了上一層函數的線性變換  
所以如果沒有 Activation Function 無論構造多複雜的 NN 最後的輸出都是輸入的線性組合  
而純粹的 Linear Combination 是無法解決更為複雜的問題  
所以常見的激活函數都是非線性的 使得 NN 可以逼近其他任何非線性函數 NN 可以應用到到更多非線性模型中

[如何理解激活函數?](https://zhuanlan.zhihu.com/p/364620596)
[激活函數](https://ithelp.ithome.com.tw/m/articles/10276865)

## Deep Learning

如果 NN consists more then three layers(include in/output) 則此 NN 被視為 Deep Neural Network  
![Deep Neural Network](<./Machine%20Learning(ML)/images/Deep%20Neural%20Network.png> "Deep Neural Network")  
Deep Machine Learning 不一定需要標籤資料集 他可以攝取原始形式的非結構化數據 並可以自動區分各資料的一組特徵
演算法不需要人工干預就可以發現資料分組的隱藏模式 -非監督式學習(Unsupervised Learning)

所以 ML 跟 DL 兩者之間其實是同一研究領域 兩者的主要區別在於 NN 的層數  
判斷: 是否超過三層? 以及是否需要人工干預來標記數據(特徵)?

[IBM Technology: Machine Learning vs Deep Learning](https://www.youtube.com/watch?v=q6kJ71tEYqM)

# 安裝問題

## 建立 Tensorflow 的 Anaconda 虛擬環境 & Solve issuse

### 1.建立&切換工作目錄

<pre>
md \pythonwork
cd \pythonwork
</code></pre>

### 2.建立 Anaconda 虛擬環境

<pre>
conda create --name tensorflow python=3.5 anaconda
</code></pre>

這邊我原本是照著書本上的使用 cmd，但無法辨識"conda"的 comand，所以我用 anaconda prompt 也能正常運行

|      comand       |                    用途                     |
| :---------------: | :-----------------------------------------: |
|   conda create    |                建立虛擬環境                 |
| --name tensorflow |           虛擬環境命名:tensorflow           |
|    python=3.5     |                   version                   |
|     anaconda      | 建立虛擬環境時 也會同時安裝其他 python 軟件 |

安裝完成後:

![註解1](/images/1.png "1")

啟動&關閉:  
書本上是教更新前的指令來退出 tensorflow 虛擬環境:

<pre>
deactivate tensorflow
</code></pre>

現在不需要在後面添加要退出的 python name of envirement 了，只需要輸入:

<pre>
conda deactivate
</code></pre>

![註解2](/images/2.png "2")

### 3.在 Anaconda 虛擬環境安裝 Tensorflow & Keras

<pre>
activate tensorflow
pip install tensorflow
pip install Keras
</code></pre>

我自己是出現這個問題:

![註解3](/images/3.png "3")

會遇到這個問題是因為安裝 Anaconda 的時候沒有新增[環境變數]  
因此使用者必須手動加入  
在[搜尋]列中輸入[環境變數]，點擊[編輯系統環境變數]  
路徑通常可以在「C:\Users\使用者名稱\anaconda3\Scripts」目錄底下可以找到

[重啟]命令提示列，再次輸入[jupyter notebook]  
會遇到新的問題：「ImportError: DLL load failed: 找不到指定的模組。」  
要解決這個問題，得將相關模組的路徑也加入環境變數  
這個路徑通常在「C:\Users\使用者名稱\anaconda3\Library\bin」回去編輯環境變數，再次新增變數路徑。  
再次重啟就成功了

開啟 jupyter notebook 後會遇到這個問題  
![註解4](/images/4.png "4")
把 command 改成這樣重新下載，問題就解決了

<pre>
pip3 install tensorflow
</code></pre>

在 import pandas 的時候又會找不到 module  
![註解5](/images/5.png "5")  
所以我去 cmd 進入 python 後輸入

<pre>
import pandas
</code></pre>

他給我了這個說明:

```
(to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)
but was not found to be installed on your system.
If this would cause problems for you,
please provide us feedback at https://github.com/pandas-dev/pandas/issues/54466
```

那我去論壇上找了很多 solution，發現很多人跟我遇到一樣的問題  
解決方法很多，但 8 成沒用  
最後是看到這個

```
Pyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),
(to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)
but was not found to be installed on your system.
If this would cause problems for you,
```

Pyarrow 好像是下一個版本的主要組件，安裝後就解決了(使用 cmd 的 python 沒問題了而已)

<pre>
pip install pyarrow
</code></pre>

結果 Jupyter notebook 打開來還是一樣 no module named 'pandas'  
用 anaconda prompt 安裝，jupyter notebook 就不會再該該叫了

<pre>
conda install pandas
</code></pre>

參考網址:  
[解決本地端 python](https://saturncloud.io/blog/how-to-fix-modulenotfounderror-no-module-named-pandas/)  
[解決 jupyther notebook](https://saturncloud.io/blog/jupyter-notebook-no-module-named-pandas/)

第一個下載 Mnist 資料、讀取+查看沒問題了，終於可以開始學東西了 TAT

![註解6](/images/5.png "6")  
[關於 keras.utils problem](https://github.com/ShawnHymel/computer-vision-with-embedded-machine-learning/blob/master/1.2.3%20-%20Training%20an%20Image%20Classifier%20with%20Keras/image_classifier_dnn.ipynb)

顯示影像需要:

<pre>
conda install matplotlib
</code></pre>
