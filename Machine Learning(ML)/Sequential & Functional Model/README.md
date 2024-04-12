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
