import numpy as np
import pandas as pd

from sklearn import datasets
boston = datasets.load_boston()

print(boston.data)
x = boston.data
t = boston.target
print(x.shape)
print(t.shape)

#データセットを分割する関数
from sklearn.model_selection import train_test_split

x_train,x_test,t_train,t_test = train_test_split(x,t,test_size=0.3,random_state=0)

#モデル・目的関数・最適化手法を決める
from sklearn.linear_model import LinearRegression
#モデルの定義
reg_model = LinearRegression()
#モデルの訓練
reg_model.fit(x_train,t_train)
#訓練後のパラメータ
w = reg_model.coef_
b = reg_model.intercept_
print(w)
print(b)
score = reg_model.score(x_train,t_train)
print(score)
# 予測値
print(reg_model.predict(x_test[:1]))
print(t_test[0])
# 決定係数
print(reg_model.score(x_test,t_test))
