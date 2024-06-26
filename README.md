# What are the different between ML and DL?

釐清前對於 AI 我是毫無頭緒 甚至不知道從何開始學起  
所以在學習前我想先搞懂 ML、DL 還有一些 NN、CNN、RNN...等等之間的關係  
還有像是 TensorFlow、OpenCV、BERT 是做甚麼用的等等...

Deep Learning => Neural Network => Machine Learning => AI

![Artificial Intelligence](<./Machine%20Learning(ML)/images/Artificial%20Intelligence.png> "AI")

## Machine Learning

我們定義模型中的權重(weight) 並使用激活函數(Activation Function)來計算  
Classical Machine Learning 更依賴人類干預來學習 由我們來定義特徵的層次結構來理解資料輸入之間的差異 過程包括人工干預/人工監督 (human supervision)

### What is Activation Function?

在 NN 中 我們會發現在每一層的 NN 輸出後都會使用一個函數(Sigmoid, Tanh, ReLU...)對結果進行運算 這個函數就是激活函數  
而 Activation Function 就是在幫助機器學習資料中的複雜模式  
激活函數分為線性(如: f(x)=x) / 非線性激活函數(如: Sigmoid, Tanh, ReLU, LReLU, PReLU, Swish)

因為 NN 中的每個 Layer 的 in/output 都是線性求和的過程 下一層的輸出只是承接了上一層函數的線性變換  
所以如果沒有 Activation Function，無論構造多複雜的 NN 最後的輸出都是輸入的線性組合 而純粹的 Linear Combination 是無法解決更為複雜的問題  
所以常見的激活函數都是非線性的 使得 NN 可以逼近其他任何非線性函數 NN 可以應用到更多非線性模型中

詳細我寫在 README.md 的 Activation Functions 部分：  
[Machine Learning Activation Function](<./Machine%20Learning(ML)/README.md>)

## Deep Learning

如果 NN consists more then three layers(include in/output) 則此 NN 被視為 Deep Neural Network (DNN)  
![Deep Neural Network](<./Machine%20Learning(ML)/images/Deep%20Neural%20Network.png> "Deep Neural Network")  
Deep Machine Learning 不一定需要標籤資料集 他可以攝取原始形式的非結構化數據 並可以自動區分各資料的一組特徵  
演算法不需要人工干預就可以發現資料分組的隱藏模式 -非監督式學習(Unsupervised Learning)

所以 ML 跟 DL 兩者之間其實是同一研究領域 兩者的主要區別在於 NN 的層數  
判斷: 是否超過三層? 以及是否需要人工干預來標記數據(特徵)?

[IBM Technology: Machine Learning vs Deep Learning](https://www.youtube.com/watch?v=q6kJ71tEYqM)

## Machine Learning Project(NTU)

|                    |                                                                Topic                                                                 |                      platform                       |
| :----------------: | :----------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------: |
|     Regression     |               [COVID-19 Cases Prediction](<./Machine%20Learning(ML)/Homework/HW1/COVID-19%20Cases%20Prediction.ipynb>)               | [Kaggle](https://www.kaggle.com/c/ml2021spring-hw1) |
|   Classification   | [TIMIT framewise phoneme classification](<./Machine%20Learning(ML)/Homework/HW2/TIMIT%20framewise%20phoneme%20classification.ipynb>) | [Kaggle](https://www.kaggle.com/c/ml2021spring-hw2) |
|        CNN         |                                       [Hw3](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|   Self-Attention   |                                       [Hw4](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|    Transformer     |                                       [Hw5](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|        GAN         |                                       [Hw6](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|        BERT        |                                       [Hw7](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
| Anomaly Detection  |                                       [Hw8](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|   Explainable AI   |                                       [Hw9](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|       Attack       |                                      [Hw10](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|     Adaptation     |                                      [Hw11](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|         RL         |                                      [Hw12](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|    Compression     |                                      [Hw13](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
| Life-Long Learning |                                      [Hw14](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |
|   Meta Learning    |                                      [Hw15](<./Machine%20Learning(ML)/Homework/Regression.py>)                                       |                        Link                         |

## Applied Deep Learning Project(NTU)

|       Topic        |                                       Link                                        | Link |
| :----------------: | :-------------------------------------------------------------------------------: | ---- |
|     Regression     | [COVID-19 Cases Prediction](<./Machine%20Learning(ML)/Homework/Regression.ipynb>) | Link |
|   Classification   |           [Hw2](<./Machine%20Learning(ML)/Homework/Classification.py>)            | Link |
|        CNN         |             [Hw3](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|   Self-Attention   |             [Hw4](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|    Transformer     |             [Hw5](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|        GAN         |             [Hw6](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|        BERT        |             [Hw7](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
| Anomaly Detection  |             [Hw8](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|   Explainable AI   |             [Hw9](<./Machine%20Learning(ML)/Homework/Regression.py>)              | Link |
|       Attack       |             [Hw10](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |
|     Adaptation     |             [Hw11](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |
|         RL         |             [Hw12](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |
|    Compression     |             [Hw13](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |
| Life-Long Learning |             [Hw14](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |
|   Meta Learning    |             [Hw15](<./Machine%20Learning(ML)/Homework/Regression.py>)             | Link |

## Practical Applications of Artificial Intelligence Project(NQU)

|                              Topic                              |                                                                      Link                                                                       | Slide                                                                                                                                                                |
| :-------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       Attribute selection mechanism for diabetes dataset        |                                                                      None                                                                       | [HW1](https://www.canva.com/design/DAF_USMT4ig/DyphS_FPmvEA6rkQhmCAmw/edit?utm_content=DAF_USMT4ig&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
| Classifying Handwritten Digits Using Multilayer Perceptron(MLP) | [Link](<./Machine%20Learning(ML)/Deep%20Neural%20Network(DNN)/Classifying%20Handwritten%20Digits%20Using%20Multilayer%20Perceptron(MLP).ipynb>) | None                                                                                                                                                                 |
|                     Mnist dataset using CNN                     |                  [HW2](<./Machine%20Learning(ML)/Convolutional%20Neural%20Network(CNN)/Mnist%20datasets%20using%20CNN.ipynb>)                   | None                                                                                                                                                                 |
|                       Cifar-10 using CNN                        |                      [HW3](<./Machine%20Learning(ML)/Convolutional%20Neural%20Network(CNN)/CIFAR-10%20using%20CNN.ipynb>)                       | None                                                                                                                                                                 |
|              Titanic Survived Prediction using MLP              |               [HW4](<./Machine%20Learning(ML)/Deep%20Neural%20Network(DNN)/Titanic%20Survived%20Prediction%20using%20MLP.ipynb>)                | None                                                                                                                                                                 |
|                    IMDB Movie Analysis(MLP)                     | [HW5](<./Machine%20Learning(ML)/Deep%20Neural%20Network(DNN)/Classifying%20Handwritten%20Digits%20Using%20Multilayer%20Perceptron(MLP).ipynb>)  | None                                                                                                                                                                 |
|                    IMDB Movie Analysis(RNN)                     |                      [HW6](<./Machine%20Learning(ML)/Recurrent%20Neural%20Network(RNN)/IMDb%20data%20analysis(RNN).ipynb>)                      | None                                                                                                                                                                 |
|                    IMDB Movie Analysis(LSTM)                    |                     [HW7](<./Machine%20Learning(ML)/Recurrent%20Neural%20Network(RNN)/IMDb%20data%20analysis(LSTM).ipynb>)                      | None                                                                                                                                                                 |
|                           Tensorflow                            |                                               [HW8](<./Machine%20Learning(ML)/Tensorflow.ipynb>)                                                | None                                                                                                                                                                 |

## My Project

|                  Topic                  |                                                        Description                                                        | Code Link                                                                              | Slide Link                                                                                                                                                                              |
| :-------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stock prediction using machine learning |                 Stock prediction using machine learning.Find the best way to solve the investment problem                 | [Midterm Project](<./Data Analysis/project/Predict stock price.ipynb>)                 | [Stock prediction Slide](https://www.canva.com/design/DAF_WjAL4As/aVMomh_VPh9QjjOxYeeefw/edit?utm_content=DAF_WjAL4As&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
| Stock prediction using machine learning | Comparing the accuracy of using multiple models and different parameters/methods in machine learning for stock prediction | [Final Project](<./Machine%20Learning(ML)/Project/Stock%20prediction(version2).ipynb>) | [Stock prediction Slide](https://www.canva.com/design/DAGDs5Qc2w8/fz7__DY-xgxcs01sMIad7g/edit?utm_content=DAGDs5Qc2w8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
|              Data Analysis              |                   Use machine learning to predict stock price movements and analyze investment patterns                   | [Code of Data Analysis](./Data%20Analysis/Project/)                                    | [Data Analysis Slide](https://www.canva.com/design/DAF-rhnq5Ec/hGco6thlPsR0iYW6jpAZqA/edit?utm_content=DAF-rhnq5Ec&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)    |
|           Statistics and Life           |                                  Explain the role of visual plotting in machine learning                                  | [Code of Data Analysis](./Data%20Analysis/Project/)                                    | [Data Analysis Slide](https://www.canva.com/design/DAGFSMNQlsE/gerRwio2vLdhixYbspj85w/edit?utm_content=DAGFSMNQlsE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)    |

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

第一個下載 Mnist 資料、讀取+查看沒問題了，終於可以開始學東西了 TAT

![註解6](/images/5.png "6")  
[關於 keras.utils problem](https://github.com/ShawnHymel/computer-vision-with-embedded-machine-learning/blob/master/1.2.3%20-%20Training%20an%20Image%20Classifier%20with%20Keras/image_classifier_dnn.ipynb)

顯示影像需要:

<pre>
conda install matplotlib
</code></pre>

### Reference:

[解決本地端 python](https://saturncloud.io/blog/how-to-fix-modulenotfounderror-no-module-named-pandas/)  
[解決 jupyther notebook](https://saturncloud.io/blog/jupyter-notebook-no-module-named-pandas/)
