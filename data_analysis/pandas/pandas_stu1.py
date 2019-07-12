'''
pandas.DataFrame 二维Series构成的数据结构，相当于表格。

pandas.DataFrame 学习一：框架的部分属性和增删改查
'''
import pandas as pd
import numpy as np

# 创建

## 生成一些时间数据列表
dates = pd.date_range('20180401', periods=6)
print(dates)

## index相当于行key，colums相当于列key
df = pd.DataFrame(data = np.random.randn(6,4), index = dates, columns = ['A','B','C','D'])
print(df)

# 属性
print(df.index) # 行key
print(list(df.index)) # 转成列表
print(df.columns) # 列key
print(df.values) # 数据
print(df.dtypes) # 每列元素的数据类型
print(df.shape) # 形状
print(df.ndim) # 维度
print(df.size) # 元素个数

# 打印数据总览信息
df.info()
print(df.describe())

# 查
## 查看头/尾几行
print(df.head(3))
print(df.tail(3))

## 查看列
print(df['A']) # df['A'] = df.A
print(df[['A', 'B']])

## 查看行
print(df[0:2])

## 支持对某一列每个元素的操作，并返回结果序列
print(df[df.B > 0])

## .loc[] 通过 key 访问
## .iloc[] 通过下标访问
print(df.loc['2018-04-04', 'B'])
print(df.iloc[0, 0])
print(df.iloc[0:1, 0:2]) # 前一行，前两列
print(df.iloc[[0,1], [0,2,3]]) # 第0、1行，第0、2、3列

# 用 DateForm 读写csv文件
df.to_csv('myfile.csv')
newdf = pd.read_csv('myfile.csv')
print(newdf)