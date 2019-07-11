'''
Series 字典与数组的结合体，既可以通过key(即index)访问，也可以通过下标访问
'''
import pandas as pd

# 创建
s1 = pd.Series(data = [1,2,3,4], index = ['a', 'b', 'c', 'd'])
print(s1)
s2 = pd.Series([100, 'python', 123.4])
print(s2)
s3 = pd.Series({'zhejiang':'hangzhou', 'jiangshu':'nanjing'})
print(s3)

# 属性
print(s1.index)
print(s1.name)
print(s1.values)
print(s1.dtype)

# 普通访问
print(s1['a'])
print(s1[1])
print(s1[['a', 'c']])

# .loc[] 通过index访问
# .iloc[] 通过下标访问
print(s1.loc['a'], s1.iloc[0])
print(s1.loc[['a', 'b']])

# 支持每个元素操作
print(s1[s1 > 3])

# 增改删
s1['e'] = 5
s1['a'] = 0
del s1['b']
print(s1)