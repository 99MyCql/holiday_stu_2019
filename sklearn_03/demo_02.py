'''
线性回归模型评估指标示例
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

"""
# 利用 diabetes数据集来学习线性回归  
# diabetes 是一个关于糖尿病的数据集， 该数据集包括442个病人的生理数据及一年以后的病情发展情况。   
# 数据集中的特征值总共10项, 如下:  
    # 性别  
    #体质指数  
    #血压  
    #s1,s2,s3,s4,s4,s6  (六种血清的化验数据)  
    #但请注意，以上的数据是经过特殊处理， 10个数据中的每个都做了均值中心化处理，然后又用标准差乘以个体数量调整了数值范围。
    #验证就会发现任何一列的所有数值平方和为1.   
"""
# Load the diabetes dataset
diabetes = datasets.load_diabetes()  

# Use only one feature  
# 增加一个维度，得到一个体质指数数组[[1],[2],...[442]]
diabetesX = diabetes.data[:, np.newaxis, 2]
#print(X)
 
# Split the data into training/testing sets
X_train = diabetesX[0:-20]
X_test = diabetesX[-20:]
 
# Split the targets into training/testing sets
y_train = diabetes.target[:-20]
y_test = diabetes.target[-20:]

# Create linear regression object
lr = linear_model.LinearRegression()
 
# Train the model using the training sets
lr.fit(X_train, y_train)
 
# Make predictions using the testing set
y_pred = lr.predict(X_test)
 
# The coefficients  
# 查看相关系数 
print(lr.coef_)
 
# The mean squared error  
# 均方差
# 查看残差平方的均值(mean square error,MSE) 
print(mean_squared_error(y_test, y_pred))

# Explained variance score: 1 is perfect prediction 
#  R2 决定系数（拟合优度）
# 模型越好：r2→1
# 模型越差：r2→0
print(r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()