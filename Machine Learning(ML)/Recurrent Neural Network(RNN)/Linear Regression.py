import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact # 互動元件

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data = pd.read_csv(url)
#print(data)

# y = w*x + b 並分離出x, y
x = data["YearsExperience"]
y = data["Salary"]

def plot_predict(w, b):
    y_pred=x*w+b
    plt.plot(x, y_pred, color="r", label="Predicct")

    plt.scatter(x, y, label="Real")
    #plt.scatter(x, y, marker="x", color='r') #更改標記之類的寫法
    plt.title("Seniority-Salary") #matplotlib是不支援中文的
    plt.xlabel("Seniority")
    plt.ylabel("Salary")

    # 設定x y軸最小-最大值
    plt.xlim([0, 12])
    plt.ylim([-60, 140])
    plt.legend() #顯示圖例
    plt.show()

# vscode 在interact有bug
interact(plot_predict, w=(-100, 100, 1), b=(-100, 100, 1)) #參數是(函數, x1(範圍,範圍, 間距), y1(範圍,範圍, 間距))

#  tutorial (https://www.youtube.com/watch?v=vtC5laIgMJc)