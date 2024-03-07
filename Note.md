## Machine Learning = Regression + Classification + Structured Learning(create somethin with structure)  

 * step1. Function  
***Model:***
  ```
  y=b+wx
  ```
 * step2. Define Loss from Training data(Loss is afunction of parameters e.g. L(b,w) )
Loss: L=1/N( Σ(e) ) e為每筆資料的預設跟實際的誤差，N為總資料數  
Loss越大代表參數越差  
計算誤差的方式:  
e=|y-y'| L is mean absolute error(MAE)  
e=(y-y')^2 L is mean square error(MSE)  
如果y為機率表示的話=>Cross-entropy  

 * step3. Optimization  


## Cross-entropy  
cross-entropy是用來觀測預測的機率分布與實際機率分布的誤差範圍  
corss-entropy越高，代表內涵的資訊量越大，不確定越多，誤差越高  
[參考資料 何謂 Cross-Entropy (交叉熵)](https://r23456999.medium.com/%E4%BD%95%E8%AC%82-cross-entropy-%E4%BA%A4%E5%8F%89%E7%86%B5-b6d4cef9189d)  