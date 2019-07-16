'''
python 原生数组的不足
'''
l1 = [1, 2, 3]
print(l1 * 2)
print(l1 + l1)
print(list(map(lambda x: x * 2, l1)))

print(range(1, 100, 2))
print(list(range(1, 100, 2)))

'''
numpy 高级数组。为了弥补 python 原声数组的不足
'''
import numpy as np

# numpy 创建
a1 = np.array([1,2,3,4,5])
print(a1)

# arange(start, stop, step) 等差数列
a2 = np.arange(1, 100, 2)
print(a2)

# numpy 属性
print(a1.ndim) # 维度
print(a1.shape) # 形状
print(a1.size) # 元素个数
print(a1.dtype) # 数据类型

# 支持对每个元素的操作
print(a1 + 2)
a3 = np.array([1, 2, 3, 4, 5])
print(a1 + a3)

# 修改形状
print(a2.shape)
a2.shape = 5,10
print(a2, a2.shape)

# 返回新形状数组
a4 = a2.reshape(5,10)
a4[0][0] = 0
print(a4)
print(a4[:, 2]) # 第二列
print(a4[0:2, 0:2]) # 前两行，前两列

print(a4.min(axis=1)) # axis=1 行
print(a4.min(axis=0)) # axis=0 列