import numpy as np
import cupy as cp
import random
import time

### NumPy を使用した場合の処理時間測定 ###
def get_w_np(x,t):
    xx = np.dot(x.T,x)
    xx_inv = np.linalg.inv(xx)
    xt = np.dot(x.T,t)
    w = np.dot(xx_inv,xt)
    return w
# 一番小さいサイズの行列の準備
N = 10
x = np.random.rand(N,N)
t = np.random.rand(N,1)
w = get_w_np(x,t)
print(w)

time_start = time.time()
# - - - 処理 - - - #
w = get_w_np(x,t)
# - - - -  - - - - #
time_end = time.time()
# 経過時間
elapsed_time = time_end - time_start
print('{:.5f}sec'.format(elapsed_time))

times_cpu = []
for N in [10,100,1000,10000]:
    np.random.seed(0)
    x = np.random.rand(N,N)
    t = np.random.rand(N,1)

    time_start = time.time()
    # - - - 処理 - - - #
    w = get_w_np(x,t)
    # - - - -  - - - - #
    time_end = time.time()
    # 経過時間
    elapsed_time = time_end - time_start
    print('N={:>5}:{:8.5f}sec'.format(N,elapsed_time))
    times_cpu.append(elapsed_time)

### CuPy を用いた場合の処理時間測定 ###
def get_w_cp(x,t):
    xx = cp.dot(x.T,x)
    xx_inv = cp.linalg.inv(xx)
    xt = cp.dot(x>t,t)
    w = cp.dot(xx_inv,xt)
    return w
# NumPy を用いた乱数生成
N = 10
x_np = np.random.rand(N,N)
t_np = np.random.rand(N,1)
# NumPy の ndarray から CuPy の ndarray へ返還
x_cp = cp.asarray(x_np)
t_cp = cp.asarray(t_np)
# NumPy と CuPy の計算結果を見比べる
w_np = get_w_np(x_np,t_np)
w_cp = get_w_cp(x_cp,t_cp)
print('NumPy:',w_np)
print('CuPy:',w_cp)

# GPU の計算時間保存用
times_gpu = []
for N in [10,100,1000,10000]:
    cp.random.seed(0)
    x = cp.random.rand(N,N)
    t = cp.random.rand(N,1)
    # GPU 上での処理が終わるまでの待機
    cp.cuda.Stream.null.synchronize()
    time_start = time.time()
    # - - - 処理 - - - #
    w = get_w_np(x,t)
    # - - - -  - - - - #
    cp.cuda.Stream.null.synchronize
    time_end = time.time()
    # 経過時間
    elapsed_time = time_end - time_start
    print('N={:>5}:{:8.5f}sec'.format(N,elapsed_time))
    times_cpu.append(elapsed_time)

import tabulate
# N 毎の実行時間の差
N = [10,100,1000,10000]
times_cpu = np.asarray(times_cpu)
times_gpu = np.asarray(times_gpu)
ratio = ['{:2f}x'.format(r) for r in times_cpu / times_gpu]

# tabulate を用いてテーブルを作成
table = tabulate.tabulate(
    zip(N,times_cpu,times_gpu,ratio),
    headers=['N','NumPyでの実行時間(sec)','CuPyでの実行時間(sec)','高速化倍率'])
print(table)