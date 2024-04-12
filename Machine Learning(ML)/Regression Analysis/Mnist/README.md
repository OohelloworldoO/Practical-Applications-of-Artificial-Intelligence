## About matplotlib structure

![matplotlib structure](./images/matplotlib%20structure.png "matplotlib structure")  
(來源: https://matplotlib.org/1.5.1/faq/usage_faq.html#parts-of-a-figure)

- Figure:指的是畫布 當我們要畫圖時需要先創建一個畫布 才能在上面加各種元素

```
fig = plt.figure()
```

### Axes:

- axis 是指 x 軸、y 軸 而 axes 指的是負數形式(two dimentional 有兩個 zxis、three dimentional 有三個)
- Figure 為畫布 axes 就是要放到畫布上的任何物體
- 每次我們在 Figure 中增加一個 subplot 就是增加一套 axis
- 所以今天 Figure 中只有一張圖 那 ax 和 plt 控制的圖片就是一樣的 效果也是
- Axis: ax.axis , ax.yaxis
- 每個 axis 由豎線和數字構成(刻度&值) 每個豎線也為一個 axis 的 subplot 所以 ax.axis 也有 axes 這個對象 對每個 axes 進行編輯就會影響 xaxis 圖上的樣子

![matplotlib](./images/matplotlib.png "matplotlib")  
(來源: https://matplotlib.org/stable/users/explain/quick_start.html)

### What are the different between plt and ax?

- plt.figure():這是 matplotlib 所提供的一個 api 可以快速地透過 plt.來畫圖 但如果想要更細緻 也就是控制到更細的部分來畫圖 就要使用第二種方式
- fig,ax=plt.subplots():透過指定 figure 和 axes 來進行畫圖 對 axes 進行單獨更細緻的操作

#### step 1 導入套件和創建數據

```
import matplotlib.pyplot as plt
​
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [66, 28, 32, 58, 18, 2, 99, 77, 66, 58]
y2 = [58,2,8,10,66,32,28,58,66,66]
```

#### step 2 創建畫布

```
fig, ax = plt.subplots(figsize = (10, 10))
```

#### step 3 畫圖

```
ax.plot(x, y1)
ax.plot(x, y2)
```

#### step 4 設定標題

```
## 標題
ax.set_title('Method 2')
ax.set_xlabel('Label X', fontsize = 'x-large', fontfamily = 'sans-serif', color = 'white', fontstyle = 'italic')
ax.set_ylabel('Label Y', fontsize = 10, fontfamily = 'sans-serif', color = 'blue', fontstyle = 'oblique')
```

#### step 5 設定 x 軸和 y 軸屬性

```
## x y軸的屬性設定
## aspect : {'auto', 'equal'} or num
ax.set_aspect('auto')
## 於軸上顯示較小的刻度
ax.minorticks_on()
## 設定x軸的範圍
ax.set_xlim(0, 8)
## 設定網格
## which : {'major', 'minor', 'both'}
ax.grid(which = 'major', axis = 'both')
```

#### Step 6 設定坐標軸 tick 和更多細節

```
## 設定座標軸tick和更多細節
​
## 設定x軸字體(旋轉、大小、顏色)
ax.xaxis.set_tick_params(rotation = 50, labelsize = 20, colors = 'w')
## 取得x軸範圍
start, end = ax.get_xlim()
## 設定x軸刻度以0.5為單位
ax.xaxis.set_ticks(np.arange(start, end, 0.5))
## 將y軸刻度顯示在右邊
ax.yaxis.tick_right()
```

# Reference:

[解決本地端 python](https://saturncloud.io/blog/how-to-fix-modulenotfounderror-no-module-named-pandas/)  
[解決 jupyther notebook](https://saturncloud.io/blog/jupyter-notebook-no-module-named-pandas/):

[你真的知道 plt / ax / fig 是什麼嗎?](https://chwang12341.medium.com/%E7%A8%8B%E5%BC%8F%E8%A7%80%E5%BF%B5-%E5%A4%A7%E5%AE%B6%E9%83%BD%E6%9C%83%E4%BD%BF%E7%94%A8plt%E7%95%AB%E5%9C%96-%E4%BD%86%E6%98%AF%E4%BD%A0%E7%9C%9F%E7%9A%84%E7%9F%A5%E9%81%93plt-ax-fig%E6%98%AF%E4%BB%80%E9%BA%BC%E5%97%8E-%E6%80%8E%E9%BA%BC%E7%94%A8-6f0bc6404f8f)  
[matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html)  
[資料分析 & 機器學習](https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC2-2%E8%AC%9B-%E5%A6%82%E4%BD%95%E7%8D%B2%E5%8F%96%E8%B3%87%E6%96%99-google-map-api-beb7c88dc4e3)  
[Cross Entropy](https://r23456999.medium.com/%E4%BD%95%E8%AC%82-cross-entropy-%E4%BA%A4%E5%8F%89%E7%86%B5-b6d4cef9189d)  
[Tensor](https://medium.com/hunter-cheng/%E6%A9%9F%E4%BD%95%E7%82%BA%E5%BC%B5%E9%87%8F-tensor-%E4%B8%89%E5%88%86%E9%90%98%E5%9C%96%E8%A7%A3%E9%A1%9E%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF%E5%9F%BA%E6%9C%AC%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-ab0ccd115aff)
[machine learning](https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_convolutional_neural_networks_work.html)
[CNN](https://colah.github.io/posts/2014-07-Conv-Nets-Modular/)
[What is convolution?!](https://www.youtube.com/watch?v=KuXjwB4LzSA)
[CNN fliter](https://ithelp.ithome.com.tw/articles/10187424)
[CNN](https://www.youtube.com/watch?v=KuXjwB4LzSA)
