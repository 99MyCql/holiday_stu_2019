import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import  Series, DataFrame
# row_dim = 3
# col_dim = 3
# zero_tsr = tf.zeros([row_dim, col_dim])
# one_tsr = tf.ones([row_dim, col_dim])
# filled_tsr = tf.fill([row_dim, col_dim], 42)
# const_tsr = tf.constant([1, 2, 3])
#
# my_var = tf.Variable(zero_tsr)
#
# print(zero_tsr)
# print(one_tsr)
# print(filled_tsr)
# print(const_tsr)
# print(my_var)
#
# sess = tf.Session()
# initialize_op = tf.global_variables_initializer()
# sess.run(initialize_op)
#####
# 数据训练
#####
data = pd.read_csv('./titanik/train.csv')
#print(data)
print(data.columns)
"""
Index(['PassengerId', 'Survived'生存情况 1 存活 0 死亡, 'Pclass' 客舱等级1=1st 2=2st 3=3st , 'Name' 乘客名字, 'Sex' 性别, 'Age' 年龄, 'SibSp' 在船兄弟姐妹数、配偶数,
       'Parch' 在船父母数、子女数, 'Ticket' 船票编号, 'Fare' 船票价格, 'Cabin' 客舱号, 'Embarked' 登船港口],
      dtype='object')
"""
data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']]
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Cabin'] = pd.factorize(data.Cabin)[0]
data.fillna(0, inplace=True)
data['Sex'] = [1 if x =='male' else 0 for x in data.Sex]

data['p1'] = np.array(data['Pclass'] == 1).astype(np.int32)
data['p2'] = np.array(data['Pclass'] == 2).astype(np.int32)
data['p3'] = np.array(data['Pclass'] == 3).astype(np.int32)

del data['Pclass']

data.Embarked.unique()
# array(['S', 'C, 'Q', 0]), dtype=object)
data['e1'] = np.array(data['Embarked'] == 'S').astype(np.int32)
data['e2'] = np.array(data['Embarked'] == 'C').astype(np.int32)
data['e3'] = np.array(data['Embarked'] == 'Q').astype(np.int32)

del data['Embarked']
# # 测试
# print(data)

data.values.dtype

data_train = data[[ 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'p1', 'p2', 'p3', 'e1', 'e2', 'e3']]

data_target = data['Survived'].values.reshape(len(data), 1)

np.shape(data_train), np.shape(data_target)
# 测试
# (891, 12)  (891, 1)
# print(np.shape(data_train))
# print(np.shape(data_target))

x = tf.placeholder("float", shape=[None, 12])
y = tf.placeholder("float", shape=[None, 1])

weight = tf.Variable(tf.random_normal([12, 1]))
bias = tf.Variable(tf.random_normal([1]))
output = tf.matmul(x, weight) + bias
pred = tf.cast(tf.sigmoid(output) > 0.5, tf.float32)

loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=output))

train_step = tf.train.GradientDescentOptimizer(0.0003).minimize(loss)

accuracy = tf.reduce_mean(tf.cast(tf.equal(pred, y), tf.float32))

#####
# 数据测试
#####
data_test = pd.read_csv('./titanik/test.csv')
data_test = data_test[[ 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']]
data_test['Age'] = data_test['Age'].fillna(data_test['Age'].mean())
data_test['Cabin'] = pd.factorize(data_test.Cabin)[0]
data_test.fillna(0, inplace=True)
data_test['Sex'] = [1 if x =='male' else 0 for x in data_test.Sex]
data_test['p1'] = np.array(data_test['Pclass'] == 1).astype(np.int32)
data_test['p2'] = np.array(data_test['Pclass'] == 2).astype(np.int32)
data_test['p3'] = np.array(data_test['Pclass'] == 3).astype(np.int32)
# array(['S', 'C, 'Q', 0]), dtype=object)
data_test['e1'] = np.array(data_test['Embarked'] == 'S').astype(np.int32)
data_test['e2'] = np.array(data_test['Embarked'] == 'C').astype(np.int32)
data_test['e3'] = np.array(data_test['Embarked'] == 'Q').astype(np.int32)

del data_test['Pclass']
del data_test['Embarked']

test_label = pd.read_csv('./titanik/gender_submission.csv')
test_label = np.reshape(test_label.Survived.values.astype(np.float32), (418, 1))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
loss_train = []
train_acc = []
test_acc = []

# # test数据集测试
# print(data_test)

for i in range(25000):
    index = np.random.permutation(len(data_target))   # 乱序处理 防止过拟合
    data_train = data_train.take(index)     # 把()写成[]了  一直报错 哈哈
    data_target = data_target.take(index)
    for n in range(len(data_target) // 100 + 1):
        batch_xs = data_train[n * 100 : n * 100 + 100]
        batch_ys = data_target[n * 100 : n * 100 + 100]
        batch_ys = batch_ys.reshape(len(batch_ys), 1)
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    if i%1000 == 0:
        loss_temp = sess.run(loss, feed_dict={x: batch_xs, y: batch_ys})
        loss_train.append(loss_temp)
        train_acc_temp = sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys})
        train_acc.append(train_acc_temp)
        test_acc_temp = sess.run(accuracy, feed_dict={x: data_test, y: test_label})
        test_acc.append(test_acc_temp)
        print(loss_temp, train_acc_temp, test_acc_temp)

# 建议写到最前面去
# import matplotlib.pyplot as plt

plt.plot(loss_train, 'k-')
plt.title('train loss')
plt.show()

plt.plot(train_acc, 'b-', label = 'train_acc')
plt.plot(test_acc, 'r--', label = 'test_acc')
plt.title('train and test accuracy')
plt.legend()
plt.show()