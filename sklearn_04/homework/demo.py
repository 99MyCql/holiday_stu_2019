'''
自行车租聘预测
数据内容：
(1) datetime：日期，以年-月-日 小时的形式给出。
(2) season：季节。1 为春季, 2为夏季,3 为秋季,4 为冬季。
(3) hodliday：是否为假期。1代表是，0代表不是。
(4) workingday：是否为工作日，1代表是，0代表不是。
(5) weather:天气
    1: 天气晴朗或者少云/部分有云。
    2: 有雾和云/风等。
    3: 小雪/小雨，闪电及多云。
    4: 大雨/冰雹/闪电和大雾/大雪。
(6) temp - 摄氏温度。
(7) atemp - 体感温度。
(8) humidity - 湿度。
(9) windspeed - 风速。
(10) casual - 非注册用户租界数量
(11) registered - 注册用户租界数量。
(12) count - 总租车数，即casual+registered数目。
'''
import pandas as pd
import numpy as np
from sklearn import preprocessing
from matplotlib.pyplot import plot as plt

df = pd.read_csv("data.csv") 
# print(df.head())
# print(df.info())

# 数据处理
# print(pd.DatetimeIndex(df.datetime))
df['hour'] = pd.DatetimeIndex(df.datetime).hour
df['day'] = pd.DatetimeIndex(df.datetime).dayofweek
df['month'] = pd.DatetimeIndex(df.datetime).month
# print(df.head())
df_origin = df 
df = df.drop(['datetime','casual','registered'], axis = 1)
print(df.head())
print(df.info())

# 划分数据和结果
X = df.drop(['count'], axis = 1).values
y = df['count'].values
# print(X.shape)
# print(y.shape)

# 特征数据标准化
X = preprocessing.scale(X)
# y = preprocessing.scale(y)

# 岭回归
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
print("======>岭回归")
from sklearn import linear_model
## cross_val_score交叉验证
score = cross_val_score(linear_model.Ridge(), X, y, scoring='r2', cv=5)
print(score)

## k折法交叉验证
kf = KFold(n_splits=5)
for train, test in kf.split(X):
    ridgeModel = linear_model.Ridge().fit(X[train], y[train])
    print("train score: {0:.3f}, test score: {1:.3f}\n".format(
        ridgeModel.score(X[train], y[train]),
        ridgeModel.score(X[test], y[test])))
    #{0:.3f} 0表示第一个参数，保留三位小数，是训练集上的得分
    #{1:.3f} 1表示测试集上的得分

# 支持向量回归
print("======>支持向量机 svm.SVR(kernel ='rbf', C = 10, gamma = .001)")
from sklearn import svm
svr = svm.SVR(kernel = 'rbf', C = 10, gamma = .001)
score = cross_val_score(svr, X, y, scoring='r2', cv=5)
print(score)

# 随机森林回归
print("======>随机森林回归 RandomForestRegressor(n_estimators = 100)")
from sklearn.ensemble import RandomForestRegressor
score = cross_val_score(RandomForestRegressor(n_estimators = 100), X, y, scoring='r2', cv=5)
print(score)

# 决策回归树
print('======>决策回归树 DecisionTreeRegressor()')
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
score = cross_val_score(tree, X, y, scoring='r2', cv=5)
print(score)

# GBDT回归
print('======>GBDT回归')
from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor()
score = cross_val_score(gbr, X, y, scoring='r2', cv=5)
print(score)