import pandas as pd
# データセットの読み込み
df = pd.read_csv('california_housing_train.csv')
print(type(df))
print(df.head())
print(df.head(3))
print(df['longitude'].head(3))
print(df.to_csv('sample.csv'))
print(df.shape)
print(df.mean()) # 平均
print(df.var()) # 分散
print(df.count()) # 各列のNOne,NoN,NoT のいずれでもない値の数
print(df.describe()) # データの概要
print(df.corr()) # 相関係数の算出

#total_rooms 列の値を昇順に並び替え
df_as = df.sort_values(by='total_rooms')
print(df_as.head())
#total_rooms 列の値を降順に並び替え
df_de = df.sort_values(by='total_rooms',ascending=False)
print(df_de.head())

print(df.head())
print(df.iloc[0,0])
print(df.iloc[1,1])
t = df.iloc[:,-1] # 全ての行の最後の列を選択
print(t.head(3))
print(type(t))
x = df.iloc[:,0:-1] # 全ての行の、先頭の列から末尾の列のひとつ手前までを選択
print(x.head(3))
x = df.iloc[:,:-1]
print(x.head(3))
print(type(x))

# median_house_value 列を選択し、全要素に対し70000より大きいかどうかを計算
mask = df['median_house_value'] > 70000
print(mask.head())
print(df[mask].head())
# 70000より小さい、または80000より大きい
mask2 = (df['median_house_value'] < 70000) | (df['median_house_value'] > 80000)
print(mask2.head())
print(df[mask2].head())
# 70000より大きい、かつ80000より小さい
mask3 = (df['median_house_value'] > 70000) & (df['median_house_value'] < 80000)
print(mask3.head())
print(df[mask3].head())

# 新しい列 taget を None で初期化
df['target'] = None
print(df.head())
mask1 = df['median_house_value'] < 60000
mask2 = (df['median_house_value'] >= 60000) & (df['median_house_value'] < 70000)
mask3 = (df['median_house_value'] >= 70000) & (df['median_house_value'] < 80000)
mask4 = df['median_house_value'] >= 80000
df.loc[mask1,'target'] = 0
df.loc[mask2,'target'] = 1
df.loc[mask3,'target'] = 2
df.loc[mask4,'target'] = 3
print(df.head())

# 欠損値を人為的に作成
df.iloc[0,0] = None
print(df.head())
# 欠損値のあるレコードを削除
df_dropna = df.dropna()
print(df_dropna.head())
mean = df.mean()
print(mean)
# 欠損値を mean で補完
df_fillna = df.fillna(mean)
print(df_fillna.head())

print(type(df))
print(type(df.values))
print(df.values)
print(type(df['longitude']))
print(type(df['longitude'].values))

import numpy as np
import random
# ndarray -> pd.DataFrame
df = pd.DataFrame(
    data=np.random.rand(10,10)
)
print(df)
