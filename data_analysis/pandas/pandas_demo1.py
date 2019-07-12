'''
大学生薪资排行榜
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('salary.csv')
print(df.info())
print(df.columns)
print(df.describe())

print(df['category'].value_counts()) # 高校的类别频率
plt.plot(df['category'].value_counts())
# plt.show()
print(df['province'].value_counts()) # 高校的所属省份频率
print(df.groupby('province')['985'].sum().sort_values(ascending=False))
print(df.groupby('category').agg(['max', 'min', 'mean'])[['2017', '2015', '2013']])

dfjs = df[df['province'] == '江苏'] # 取出省份为江苏
print(dfjs)