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
![註解2](/images/2.png "2")

### 3.在Anaconda虛擬環境安裝Tensorflow & Keras  
<pre>
activate tensorflow
pip install tensorflow
pip install Keras
</code></pre>