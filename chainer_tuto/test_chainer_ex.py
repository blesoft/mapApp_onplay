# データセットの準備
from sklearn.datasets import load_iris

x,t = load_iris(return_X_y=True)
x = x.astype('float32')
t = t.astype('int32')

# Tuple Dataset
from chainer.datasets import TupleDataset
dataset = TupleDataset(x,t)
# print(dataset[0])
# print(dataset[:2])
## データセット分割
from chainer.datasets import split_dataset_random
train_val,test = split_dataset_random(dataset,int(len(dataset) * 0.7),seed=0)
train,valid = split_dataset_random(train_val,int(len(train_val) * 0.7),seed=0)
## SerialIterator
from chainer.iterators import SerialIterator
train_iter = SerialIterator(train,batch_size=4,repeat=True,shuffle=True)
minibatch = train_iter.next()
print(minibatch)

# ネットワーク決定
## Chain
import chainer
import chainer.links as L
import chainer.functions as F

class Net(chainer.Chain):
    def __init__(self,n_in=4,n_hidden=3,n_out=3):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_in,n_hidden)
            self.l2 = L.Linear(n_hidden,n_hidden)
            self.l3 = L.Linear(n_hidden,n_out)
    def forward(self,x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        h = self.l3(h)
        return h
net = Net()

from chainer import optimizers
from chainer.optimizer_hooks import WeightDecay
optimizer = optimizers.SGD(lr=0.001) # 学習率を0.01に設定
optimizer.setup(net)
for param in net.params():
    if param.name != 'b': # バイアス以外だったら
        param.update_rule.add_hook(WeightDecay(0.0001)) # 重み減衰
## 最適化手法
from chainer import optimizers
from chainer.optimizer_hooks import WeightDecay
optimizer = optimizers.MomentumSGD(lr=0.001,momentum=0.9)
optimizer.setup(net)
for param in net.params():
    if param.name != 'b': # バイアス以外だったら
        param.update_rule.add_hook(WeightDecay(0.0001)) # 重み減衰

## ネットワークを訓練
gpu_id = 0 # 仕様するGPU番号
n_batch = 64 # バッチサイズ
n_epoch = 50 # エポック数
### ネットワークをGPUメモリ上に転送
net.to_gpu(gpu_id)
### ログ
results_train,results_valid = {},{}
results_train['loss'],results_train['accuracy'] = [],[]
results_valid['loss'],results_valid['accuracy'] = [],[]
train_iter.reset() # 上で一度next()が呼ばれているため
count = 1
for epoch in range(n_epoch):
    while True:
        #### ミニバッチの取得
        train_batch = train_iter.next()
        #### xとtに分割
        ##### データをGPUに転送するために,concat_examplesにgpu_idを渡す
        x_train,t_train = chainer.dataset.concat_examples(train_batch,gpu_id)
        ##### 予測値と目的関数を計算
        y_train = net(x_train)
        loss_train = F.softmax_cross_entropy(y_train,t_train)
        acc_train = F.accuracy(y_train,t_train)
        ##### 勾配の初期化と勾配の計算
        net.cleargrads()
        loss_train.backward()
        ##### パラメータ更新
        optimizer.update()
        ##### カウントアップ
        count += 1
        ##### valid データの評価
        if train_iter.is_new_epoch:
            ####### 検証用データに対する結果の確認
            with chainer.using_config('train',False),chainer.using_config('enable_backprop',False):
                x_valid,t_valid = chainer.dataset.concat_examples(valid,gpu_id)
                y_valid = net(x_valid)
                loss_valid = F.softmax_cross_entropy(y_valid,t_valid)
                acc_valid = F.accuracy(y_valid,t_valid)
            ####### GPU上の計算結果をCPUに転送する
            loss_train.to_cpu()
            loss_valid.to_cpu()
            acc_train.to_cpu()
            acc_valid.to_cpu()
            ####### 結果の表示
            print('epoch:{},iteration:{},loss(train):{:.4f},loss(valid):{:.4f}' 'acc(train):{:.4f},acc(valid):{:.4f}'.format(
                epoch,count,loss_train.array.mean(),loss_valid.array.mean(),acc_train.array.mean(),acc_valid.array.mean()
            ))
            ####### 可視化用に保存
            results_train['loss'].append(loss_train.array)
            results_train['accuracy'].append(acc_train.array)
            results_valid['loss'].append(loss_valid.array)
            results_valid['accuracy'].append(acc_valid.array)

            break