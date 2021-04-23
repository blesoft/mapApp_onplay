import numpy as np

x = np.array([2,3,1])
t = np.array([20])

# 0-1 層間のパラメータ
w1 = np.array([[3,1,2],[-2,-3,-1]])
b1 = np.array([0,0])

# 2-3 層間のパラメータ
w2 = np.array([[3,2]])
b2 = np.array([0])

# 中間層の計算
u1 = w1.dot(x) + b1
h1 = 1. /(1 + np.exp(-u1))

# 出力の計算
y = w2.dot(h1) + b2

print(y)

dldy = -2 * (t-y) # dL / dy
dydw2 = h1 # dy / dw_2
dldw2 = dldy * dydw2 # 求めたい勾配 dL / dw_2

print(dldw2)

dydh1 = w1 # dy / dh1
dh1du1 = h1 * (1-h1) # dh1 / du1
du1dw1 = x # du1 / dw1
dldu1 = dldy / dh1du1
du1dw1 = du1dw1[None] # du1dw1は(3,)というshapeなので、g_u1w1[None]として(1,3)に変換
dldw1 = dldu1.T.dot(du1dw1) # dl / dw1 : 求めたい勾配
print(dldw1)
