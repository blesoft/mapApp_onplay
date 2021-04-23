import chainer

# print(chainer.print_runtime_info())

from sklearn.datasets import load_iris
x,t = load_iris(return_X_y=True)

# print('x=',x.shape)
# print('t=',t.shape)

x = x.astype('float32')
t = t.astype('int32')

# データセット分割
from sklearn.model_selection import train_test_split
x_train_val,x_test,t_train_val,t_test = train_test_split(x,t,test_size=0.3,random_state=0)
x_train,x_val,t_train,t_val = train_test_split(x_train_val,t_train_val,test_size=0.3,random_state=0)

# ネットワーク定義
import chainer.links as L
import chainer.functions as F
## 入力次元数が3,出力次元数が2の全結合層
l = L.Linear(3,2)
from chainer import Sequential
## net としてインスタンス化
n_input = 4
n_hidden = 10
n_output = 3

net = Sequential(
    L.Linear(n_input,n_hidden),F.relu,
    L.Linear(n_hidden,n_hidden),F.relu,
    L.Linear(n_hidden,n_output)
)
# 最適化手法を選択
optimizer = chainer.optimizers.SGD(lr=0.01)
optimizer.setup(net)

# ネットワークを訓練する
n_epoch = 30
n_batchsize = 16
import numpy as np
iteration = 0
## ログの保存
results_train = {
    'loss':[],
    'accuracy':[]
}
results_valid = {
    'loss':[],
    'accuracy':[]
}

for epoch in range(n_epoch):
    ## データセットを並び替えた順番を取得
    order = np.random.permutation(range(len(x_train)))
    ## 各バッチ毎の目的関数の出力と分類制度の保存用
    loss_list = []
    accuracy_list = []

    for i in range(0,len(order),n_batchsize):
        ### バッチを準備
        index = order[i:i+n_batchsize]
        x_train_batch = x_train[index,:]
        t_train_batch = t_train[index]
        ### 予測値を出力
        y_train_batch = net(x_train_batch)
        ### 目的関数を適用し、分類制度を計算
        loss_train_batch = F.softmax_cross_entropy(y_train_batch,t_train_batch)
        accuracy_train_batch = F.accuracy(y_train_batch,t_train_batch)
        loss_list.append(loss_train_batch.array)
        accuracy_list.append(accuracy_train_batch.array)
        ### 勾配のリセットと再計算
        net.cleargrads()
        loss_train_batch.backward()
        ### パラメータの更新
        optimizer.update()
        ### カウントアップ
        iteration += 1

    ## 訓練データに対する目的関数の出力と分類制度を集計
    loss_train = np.mean(loss_list)
    accuracy_train = np.mean(accuracy_list)

    ## 1エポック終えたら、検証データで評価
    ### 検証データで予測値を出力
    with chainer.using_config('train',False),chainer.using_config('enable_backprop',False):
        y_val = net(x_val)
    ## 目的関数を適用し、分類制度を計算
    loss_val = F.softmax_cross_entropy(y_val,t_val)
    accuracy_val = F.accuracy(y_val,t_val)

    ## 結果の表示
    print('epoch:{}, iteration:{}, loss(train):{:.4f}, loss(valid):{:.4f}'.format(
        epoch,iteration,loss_train,loss_val.array
    ))

    ## ログを保存
    results_train['loss'].append(loss_train)
    results_train['accuracy'].append(accuracy_train)
    results_valid['loss'].append(loss_val.array)
    results_valid['accuracy'].append(accuracy_val.array)

import matplotlib.pyplot as plt
# 目的関数の出力
plt.plot(results_train['loss'],label='train')
plt.plot(results_valid['loss'],label='valid')
plt.legend()
plt.show()
# 分類制度(accuracy)の出力
plt.plot(results_train['accuracy'],label='train')
plt.plot(results_valid['accuracy'],label='valid')
plt.legend()
plt.show()

# テストデータを用いた評価
with chainer.using_config('train',False),chainer.using_config('enable_backprop',False):
    y_test = net(x_test)
accuracy_test = F.accuracy(y_test,t_test)
print(accuracy_test.array)

chainer.serializers.save_npz('my_iris.net',net)

# 訓練住みネットワークを用いた推論
loaded_net = Sequential(
    L.Linear(n_input,n_hidden),F.relu,
    L.Linear(n_hidden,n_hidden),F.relu,
    L.Linear(n_hidden,n_output)
)
chainer.serializers.load_npz('my_iris.net',loaded_net)

with chainer.using_config('train',False),chainer.using_config('enable_backprop',False):
    y_test = loaded_net(x_test)

print(np.argmax(y_test[0,:].array))