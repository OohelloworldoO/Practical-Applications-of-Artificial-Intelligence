import pandas as pd
import numpy as np #Numpy是python的語言擴充程式庫 支援維度陣列 & 矩陣運算

# keras套件看READ.md
from keras import utils # 匯入keras.utils 因為後續要將label標籤轉換為One hot encoding
np.random.seed(10) # 設定seed可以讓每次需要隨機產生的資料 都有相同的output

from keras.datasets import mnist # download & read Mnist資料，需要先import mnist module 存放在C://user/username/.keras

(x_train_image, y_train_label),(x_test_image, y_test_label)=mnist.load_data()

print('train data=',len(x_train_image)) #train訓練資料:60000 筆
print('test data=',len(x_test_image)) #test測試資料:10000 筆

print('x_train_image:',x_train_image.shape) #image是單色的數字影像
print('y_train_label:',y_train_label.shape) #label是真實數值

import matplotlib.pyplot as plt

def plot_image(image): 
    fig=plt.gcf()
    fig.set_size_inches(2, 2) #設定圖形大小
    plt.imshow(image,cmap='binary') #使用plt.imshow顯示圖形，傳入parameter是28*28的graphic，cmap參數設定為binary以黑白灰階顯示
    plt.show()

plot_image(x_train_image[0])

y_train_label[0] #查看第0筆資料的真實數值