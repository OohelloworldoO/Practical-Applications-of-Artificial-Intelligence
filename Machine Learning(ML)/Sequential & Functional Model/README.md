# Seqiemtial & Function Model

## Sequential Model

顧名思義就是將 Layers 之間以線性序列的結構呈現 每一層的 output 都會做為下一層的 input  
![sequential model structure](./Images/Sequential%20model%20structure.png "sequential model structure")

```
model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
```

- 首先透過`Sequential()`來建立序列模型
- 透過`model.add()`增加 Layer 最後的為 output

## Functional model

相比於 Sequential API, Functional API 更加彈性 因為可以透過簡單的方式定義 Modle 定義每一個 Layer 間連結的關係  
![Functional model](./Images/Functional%20model.png "Functional model")

```
input_layer = layers.Input(shape=(28, 28, 1))

conv1 = layers.Conv2D(32, (3, 3), activation='relu')(input_layer)
maxpool1 = layers.MaxPooling2D((2, 2))(conv1)
conv2 = layers.Conv2D(64, (3, 3), activation='relu')(maxpool1)
maxpool2 = layers.MaxPooling2D((2, 2))(conv2)

flatten_layer = layers.Flatten()(maxpool2)

dense1 = layers.Dense(128, activation='relu')(flatten_layer)
output_layer = layers.Dense(10, activation='softmax')(dense1)

model = models.Model(inputs=input_layer, outputs=output_layer)
```

- 定義 Model 的 input_shape
- 分別建立 Hidden Layer 包含了 Convolutional 與 Max-Pooling 的組合 再將該組合的輸出 輸入 Flatten Layer
- 最後透過 Dense Layer 匯集資料作為輸出曾 最後用`Model()`方法來定義整個 Model 的 input_layer、output_layer

# Compile

## Optimizer

是一個透過更新 Model 的權重（weight）以達到損失函數最小值的演算法以下列出幾個常用的 Optimizer 與其應用範圍  
| Optimizer | Syntax | Description | Adventage | Disadventage |
| :---------------: | :-----: | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------- |
| SGD woth momentum | SGD | 最基本的最佳演算法,透過較小的單位步階沿著 Loss Function 的負梯度方向更新模型參數,同時引入累積前期的梯度項目的 momentum 來強化 SGD | 記憶體用量低 震盪較小 更新較為平順且易收斂 | 需要調配出超參數類型的 Momentum 係數 |
| RMSprop | RMSprop | 透過將學習率除以平方梯度的指數移動平均值,以調整每個參數的學習率 | 會自行透過每一個參數的學習率達到收斂 | 有時還是要自己調整學習率,有時需要衰減 |
| Adam | Adam | 結合了 Momentum 和 RMSprop 的想法,維持梯度和梯度平方的移動平均值,做到調整學習率並提供動量 | 收斂速度快,易運作於各類型神經網路架構中;有自是應學習率與較快的收斂速度 | 超參數的靈敏度低,有時要自行調整其參數 |
| Adamax | Adamax | Adam 的變形,利用過去的梯度最大值來取代 L2 的平均值進行縮放 | 比 Adam 所需調整的超參數少,能在較大梯度上順利運作 | 應用範圍不如 Adam 與 RMSprop |
| Nadam | Nadam | 將 Nesterov 的加速度與 Adam 的自適應學習率結合 | 保留 Adam 的自恃應學習率特性 | 與 Adam 相同 |

## Loss Function

損失函數量測 model 在訓練資料中的表現 選擇損失函數時取決於你要分析與建立的 model 類型  
常用的損失函數也有很多種類，分述如下：  
| Loss Function | Syntax | Description | Adventage | Disadventage |
| :---------------: | :-----: | ----------- | --------- | ------------ |
| Mean squared error(MSE) | MeanSquaredError() | 通常用於執行 Regression,會計算預測值與實際值之間的平均平方差 |適用於以梯度為基礎的最佳化處理|容易受到資料當中的離群質影響,不是用於分類任務|
| Binary crossentropy | BinaryCrossentropy() | 用於執行二元分類任務,將預測和
實際二元標記間的差異做量化 |適用於二元分類任務,並以梯度為基礎的最佳化處理|無法分類多元分類任務,容易在 Class 間的使用上出問題|
| Categorical crossentropy | CategoricalCrossentropy() | 用於多元分類任務,衡量預測的分類類別機率,與真實分類的分布之間的差異 |光飯使用於處理分類項目較多的任務|很難透過 Loss 參數值看出|
| Hinge loss | hinge_loss | 用於二元分類任務同時也支援向量機 SVMs,通過將類別間的邊緣最大化以鼓勵執行正確的分類 |編劇最大化可以做到正確分類與明顯分界,不容易收到異常值影響|對分析數據值為 0 時無法微分;無法直接應用在多元酚類的問題中|
| Kullback-Leibler divergence | kl_divergence_loss | 用於衡量兩個機率分布的差異性 |很經常應用於 VAE 等生成模型|非一般的 Loss function,以散度值呈現,無法值觀判斷 loss,KL 發散不對稱,KL(P|Q)=!KL(Q|P)|

## Metric

Metric 常用來評估模型在訓練與驗證資料的表現 選擇 Metric 時取決於你想要在模型中所得到的結論  
常用的 Metric 也有很多種類 分述如下：  
| Metric | Syntax | Description | Adventage | Disadventage |
| :---------------: | :-----: | ----------- | --------- | ------------ |
|Accuracy | SGD | Link |||
| RMSprop | RMSprop | Link |||
| Adam | Adam | Link |||
| Adamax | Adamax | Link |||
| Nadam | Nadam | Link |||

表格還沒整理完!
https://ithelp.ithome.com.tw/m/articles/10330082  
https://ithelp.ithome.com.tw/m/articles/10328680

# Reference

[优化器 optimizers - Keras 中文文档](https://keras-cn.readthedocs.io/en/latest/legacy/other/optimizers/)  
[神經網路訓練參數的特性與使用時機](https://blog.toright.com/posts/7035/keras-tutorial-parameter-algorithm)  
[Sequential & Functional Model 與 API 細節解說](https://ithelp.ithome.com.tw/m/articles/10330082)  
[Layers / Model / Module](https://ithelp.ithome.com.tw/m/articles/10328680)  
[使用 Keras 建立回歸模型](https://hackmd.io/@flagmaker/rkDYJRLwj)
[Keras 的優化器 Optimizer](https://ithelp.ithome.com.tw/articles/10304509?sc=rss.iron)
