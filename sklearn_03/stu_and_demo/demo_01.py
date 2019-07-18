'''
分类算法评估示例
使用随机森林实现分类并输出评价指标
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

"""
函数说明：绘制ROC曲线
Parameters:
     labels:测试标签列表
     predict_prob:预测标签列表
"""
def plot_roc(labels, predict_prob):
    false_positive_rate, true_positive_rate, thresholds = \
        metrics.roc_curve(labels, predict_prob)
    roc_auc = metrics.auc(false_positive_rate, true_positive_rate)  #计算AUC值
    print('AUC=' + str(roc_auc))
    plt.title('PC5-ROC')
    plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.4f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.ylabel('TPR')
    plt.xlabel('FPR')
    # plt.savefig('figures/PC5.png') #将ROC图片进行保存
    plt.show()

df = pd.read_csv('demo_01_data.csv')
print(df.info())
print(df.values)

X = df.values[:, 0:-1]
Y = df.values[:, -1]

# 标签二值化
from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
Y2 = lb.fit_transform(Y)
print(Y2.shape)
Y2.shape = 125
print(Y2)

datasets, labels = X, Y2 # 对数据集进行处理
# 训练集和测试集划分
X_train = datasets[:115]
y_train = labels[:115]
X_test = datasets[90:]
y_test = labels[90:]
# 随机森林分类器
clf = RandomForestClassifier()
clf = RandomForestClassifier(n_estimators=200, random_state=0)
clf.fit(X_train, y_train)  # 使用训练集对分类器训练
y_predict = clf.predict(X_test)  # 使用分类器对测试集进行预测

print('准确率:', metrics.accuracy_score(y_test, y_predict)) #预测准确率输出
print('宏平均精确率:',metrics.precision_score(y_test,y_predict,average='macro')) # 预测宏平均精确率输出
print('微平均精确率:', metrics.precision_score(y_test, y_predict, average='micro')) # 预测微平均精确率输出
print('宏平均召回率:',metrics.recall_score(y_test,y_predict,average='macro')) # 预测宏平均召回率输出
print('平均F1-score:',metrics.f1_score(y_test,y_predict,average='weighted')) # 预测平均f1-score输出
print('混淆矩阵输出:',metrics.confusion_matrix(y_test,y_predict)) # 混淆矩阵输出

print('分类报告:', metrics.classification_report(y_test, y_predict)) # 分类报告输出
plot_roc(y_test, y_predict) # 绘制ROC曲线并求出AUC值