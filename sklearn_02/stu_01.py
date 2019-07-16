'''
决策树。需要根据多个属性的值来决定结果的问题，通过不同属性值产生不同结果的数据训练模型，
计算出每个属性的权重，从而得出每个属性的权重，根据权重构建决策树(权重越大越是父结点)。
'''
def createDataSet():
    # 数据集
    dataSet = [[0, 0, 0, 0, 'no'],
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况'] # 分类属性
    return dataSet, labels # 返回数据集和分类属性

dataSet, labels = createDataSet()

# 获取 X 数据集
## 方法一
x1_train = [data[0:-1] for data in dataSet]
print(x1_train)

## 方法二
import numpy as np
x2 = np.array(dataSet)
x2_train = x2[:, 0:-1]
x2_train = x2_train.astype(int)
print(x2_train)

# 将数据结果 Y 标签化
from sklearn import preprocessing
y2 = x2[:, -1]
lb = preprocessing.LabelBinarizer()
y2_train = lb.fit_transform(y2)

# 建立模型训练并预测
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(x2_train, y2_train)
print(labels)
test = [0,0,1,0]
test = np.array(test)
test.shape = (1,4)
print(clf.predict(test))

# 示例
from sklearn import datasets
digits = datasets.load_digits() # 自带数据集
print(digits.keys())
print(digits.images[0])
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(digits.images[0])
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)
clf = tree.DecisionTreeClassifier(criterion='entropy') # gini 基尼系数
clf.fit(X_train, y_train)
print(clf.predict(X_test))
print(clf.score(X_test, y_test))
