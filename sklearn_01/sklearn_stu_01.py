import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def runplt():
    plt.figure()
    plt.title('匹萨价格与直径数据')
    plt.xlabel('直径（英寸）')
    plt.ylabel('价格（美元）')
    plt.axis([0, 25, 0, 25])
    plt.grid(True)
    return plt

# 数据展示
plt = runplt()
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
plt.plot(X, y, 'k.')
plt.show()

# 机器学习的方法进行预测
from sklearn.linear_model import LinearRegression
## 创建并拟合模型
model = LinearRegression() # 线性回归模型
model.fit(X, y)
print('预测一张12英寸匹萨价格：$%.2f' % model.predict([[12]])[0])

# 比较原数据与预测值
plt = runplt()
plt.plot(X, y, 'k.')
X2 = [[0], [10], [14], [25]]
model = LinearRegression()
model.fit(X, y)
y2 = model.predict(X2)
plt.plot(X, y, 'k.')
plt.plot(X2, y2, 'g-')
plt.show()

# 预测值与原数据的差的平方之和
import numpy as np
print('残差平方和: %.2f' % np.mean((model.predict(X) - y) ** 2))

# 模型评估
## 测试集
X_test = [[8], [9], [11], [16], [12]]
y_test = [[11], [8.5], [15], [18], [11]]
model = LinearRegression()
model.fit(X, y)
model.score(X_test, y_test)