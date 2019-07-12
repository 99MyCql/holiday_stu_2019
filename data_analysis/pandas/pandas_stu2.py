'''
pandas.DataFrame 学习二：框架的数理统计操作和分组
'''
import pandas as pd
import numpy as np

print('======================================')

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 
                          'foo', 'bar', 'foo', 'bar'],
                   'B' : ['one', 'one', 'two', 'three', 
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df)
print(df.describe())

# 求和
print('-------------求和---------------')
print(df.sum()) # 每列求和
print(df.sum(axis=0)) # 第0维/列求和
print(df.sum(axis=1)) # 第1维/行求和
print(df['A'].sum()) # 'A'列求和

# 求平均值，与求和类似
print('-------------求平均值---------------')
print(df.mean()) # 求平均值

# 求最大/最小值，与求和类似
print('-------------求最大最小---------------')
print(df.max())
print(df.min())

# 自定义数据处理
print('-------------自定义数据处理---------------')
print(df['A'].apply(lambda x: 1 if x == 'foo' else 0))

# 统计个数
print('-------------统计个数---------------')
print(df.count()) # 每列
print(df['A'].count())
print(list(df['A']).count('foo'))

# 统计不相同
print('-------------统计不相同---------------')
print(df['A'])
print(df['A'].unique()) # 不相同的数据
print(df['A'].nunique()) # 不相同数据的个数

# 统计频率
print('-------------统计频率---------------')
print(df['A'].value_counts())
print(df['A'].value_counts('foo'))

# 分组
print('-------------分组---------------')
print(df.groupby('B')) # 以B列的数据分组，B列中相同数据的行归为一行，其它列对应行的数据归为一组
print(df.groupby('B').count())
print(df.groupby('B', as_index=False).count())
print(df.groupby('B', as_index=False).count()['A'])
print(df.groupby(['A', 'B'], as_index=False).count())
print(df.groupby('B').max())
print(df.groupby('B').min())
print(df.groupby('B').agg(['max', 'min']))
