'''
K-Mean 聚类分析。求图中一堆点中的某点属于哪个类，类的数量由用户确定，或通过肘部法则来确定。
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
cluster2 = np.random.uniform(3.5, 4.5, (2, 10))
X = np.hstack((cluster1, cluster2)).T # 将两个二维数组先拼接，然后转置，变成 20x2
plt.figure()
plt.axis([0, 5, 0, 5])
plt.grid(True)
plt.plot(X[:,0],X[:,1],'k.')
plt.show()

# 肘部法则
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
K = range(1, 10)
meandistortions = []
for k in K:
    kmeans = KMeans(n_clusters=k) # 设置分类，建模
    kmeans.fit(X) # 20x2 训练
    if k == 9:
        print(kmeans.cluster_centers_)
        print(X)
        print(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1))
    # 每个点到 最近的类中心点 的距离之和 / 类的个数
    # cdist()点到各类中心点的距离
    meandistortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
plt.plot(K, meandistortions, 'bx-')
plt.xlabel('k')
plt.ylabel('平均畸变程度')
plt.title('用肘部法则来确定最佳的K值')
plt.show()