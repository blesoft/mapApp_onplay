import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
print(df.head())

plt.scatter(df['median_income'],df['median_house_value'])
plt.show()
plt.scatter(df['population'],df['median_house_value'])
plt.show()
plt.hist(df['median_house_value'])
plt.show()
plt.hist(df['median_house_value'],bins=50)
plt.show()
plt.boxplot(df['median_house_value'])
plt.show()
plt.boxplot((df['total_bedrooms'],df['population']))
plt.show()

import numpy as np
x = np.linspace(0,10,100)
y = x + np.random.randn(100)
plt.plot(y)
plt.show()
plt.plot(x,y)
plt.show()

import seaborn as sns
sns.distplot(df['population'])
plt.show()
sns.pairplot(df)
plt.show()