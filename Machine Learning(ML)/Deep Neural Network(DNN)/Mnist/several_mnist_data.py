import pandas as pd
import numpy as np #Numpy是python的語言擴充程式庫 支援維度陣列 & 矩陣運算
import matplotlib.pyplot as plt

# keras套件看READ.md
from keras import utils # 匯入keras.utils 因為後續要將label標籤轉換為One hot encoding
np.random.seed(10) # 設定seed可以讓每次需要隨機產生的資料 都有相同的output

from keras.datasets import mnist # download & read Mnist資料，需要先import mnist module 存放在C://user/username/.keras

(x_train_image, y_train_label),(x_test_image, y_test_label)=mnist.load_data()


def plot_imamges_labels_prediction(images, labels, prediction, idx, num=10):
    fig=plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25
    for i in range(0, num):
        ax=plt.subplot(4, 4, 1+i) #build subgraph為5*5
        ax.imshow(images[idx], cmap='binary') #劃出subgraph
        title="label=" + str(labels[idx]) #set subgraph's title
        if len(prediction)>0:
            titlet+=",predict=" + str(prediction[idx]) #title加入預測結果
        ax.set_title(title, fontsize=10) #設定子圖形的title、size
        ax.set_xticks([]);ax.set_yticks([]) #設定不顯示刻度
        idx+=1 #讀取下一筆
    plt.show()

plot_imamges_labels_prediction(x_train_image, y_train_label, [], 0, 10) #0~9筆