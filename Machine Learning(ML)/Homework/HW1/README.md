# pytorch

torch nn、utils.data、utils.tensorboard
torch.backends.cudnn
torch.manual

## Tensor

- torch.Tensor  
  創建 Tensor 包含任意維度向量
- torch.randn  
  創建 Tensor data 隨機
- torch.cat  
   concatenate Tensor
- x.view  
  reshape Tensor dimention

## Computational Graph

- autograd.Variable

- x.backward

## Functions

torch.nn 提供了很多 neural network 需要的功能和元件  
torch.nn.functional 也提供了很多常用 function  
兩者差別在於 torch.nn.functional 提供的是純函數 而 torch.nn 提供的是一個包裝完整的 nn.Module（也就是可以直接跟其它 function 鏈結起來拿去訓練了）  
API 基本上就是直接對應 function 名字 Linear、ReLU、Sigmoid 之類

## Training & Optimizer

torch.optim 裡陳列了很多 optimizer 常用的例如 SGD、Adam、RMSprop 等等

## Neural Network

基本上這個 model 就是一個 class 繼承 torch.nn.Module 只要 override `__init__` 和 `forward` 就能定義這個 model

- `__init__`  
  定義 model 中需要的參數，weight、bias 等等
- `forward`  
  定義 model 接收 input 時 data 要怎麼傳遞、經過哪些 activation function 等等

# Reference

[PyTorch 入門](https://medium.com/pyladies-taiwan/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92%E6%96%B0%E6%89%8B%E6%9D%91-pytorch%E5%85%A5%E9%96%80-511df3c1c025)
