from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
scaler = StandardScaler()
import test_scikit_learn

x_train = test_scikit_learn.x_train
x_test = test_scikit_learn.x_test
t_train = test_scikit_learn.t_train
t_test = test_scikit_learn.t_test

# 前処理
# 標準化
scaler_fit = scaler.fit(x_train)
print(scaler_fit)

# 平均
scaler_mean = scaler.mean_
print(scaler_mean)

# 分散
scaler_var = scaler.var_
print(scaler_var)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

reg_model = LinearRegression()

# モデルの訓練
reg_model.fit(x_train_scaled,t_train)

# 精度の検証(訓練データ)
score_train = reg_model.score(x_train_scaled,t_train)
print(score_train)
# 精度の検証(テストデータ)
score_test = reg_model.score(x_test_scaled,t_test)
print(score_test)

from sklearn.preprocessing import PowerTransformer
scaler = PowerTransformer()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)
reg_model = LinearRegression()
reg_model.fit(x_train_scaled,t_train)

# 訓練データでの決定係数
score_train = reg_model.score(x_train_scaled,t_train)
print(score_train)

#　テストデータでの決定係数
score_test = reg_model.score(x_test_scaled,t_test)
print(score_test)

from sklearn.pipeline import Pipeline
# パイプラインの作成
pipeline = Pipeline([
    ('scaler',PowerTransformer()),
    ('reg',LinearRegression())
])
# scaler および reg を順番に使用
pipeline_fit = pipeline.fit(x_train,t_train)

# 訓練用データセットを用いた決定係数の算出
pipeline_score = pipeline.score(x_train,t_train)
print(pipeline_score)

# テスト用データセットを用いた決定係数の算出
liner_result = pipeline.score(x_test,t_test)
print(liner_result)