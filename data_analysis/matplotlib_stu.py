'''
matplotlib.pyplot 画图工具
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

a = np.arange(1, 10, 0.2)
b = np.sin(a)

plt.figure(figsize=(10, 5)) # 生成画布
plt.plot(a, b, 'ro') # 准备数据

plt.figure()
plt.plot(a, b, color='r', linestyle='--', linewidth=3.0, label='sin')
c = np.cos(a)
plt.plot(a, c, 'g-.', label='cos')
plt.legend() # 显示图例(即不同线注解)
plt.xlabel('弧度') # x轴名称
plt.ylabel('正/余弦值') # y轴名称

plt.figure()
plt.scatter(a,b) 

plt.show() # 显示
