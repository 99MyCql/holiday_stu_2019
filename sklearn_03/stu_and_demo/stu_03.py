'''
数据标准化
'''
from sklearn import preprocessing
import numpy as np

x = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# 函数标准化
## 将每一列特征标准化为标准正太分布，注意，标准化是针对每一列而言的
x_scale = preprocessing.scale(x)
print(x_scale)

## 可以查看标准化后的数据的均值与方差，已经变成0,1了
## axis=0 表示对每一列
print(x_scale.mean(axis=0))

## 同理，看一下标准差
print(x_scale.std(axis=0))

# 类标准化
## StandardScaler()中可以传入两个参数：with_mean, with_std. 这两个都是布尔型的参数，默认情况下都是true,但也可以自定义成false.即不要均值中心化或者不要方差规模化为1.
scaler = preprocessing.StandardScaler()
## 调用fit方法，根据已有的训练数据创建一个标准化的转换器
scaler.fit(x)

# 使用上面这个转换器去转换训练数据x,调用transform方法
print(scaler.transform(x))
# 好了，比如现在又来了一组新的样本，也想得到相同的转换
new_x = [[-1., 1., 0.]]
print(scaler.transform(new_x))