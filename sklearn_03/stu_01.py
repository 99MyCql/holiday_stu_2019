'''
分类模型(如决策树)常用评估指标

二维混淆矩阵：
                                预测结果

真实类别            类别1（正例）               类别2（反例）                               

类别1（正例）   真正例(True Positive) TP    假反例(False Negatibe) FN

类别2（反例）   假正例(False Positive) FP   真反例(True Negatibe) TN
'''
print('-------------二维混淆矩阵---------------')
from sklearn.metrics import confusion_matrix
y_true =[0,0,1,0] # 真实值
y_pred = [1,0,1,0] # 预测值
# sklearn.metrics.confusion_matrix(y_true, y_pred, labels=None, sample_weight=None)
print(confusion_matrix(y_true, y_pred))
'''
  0 1
0 2 1  # 原本是0预测为0有两个，原本为0预测为1的有一个
1 0 1
'''

y_true=[2,1,0,1,2,0]
y_pred=[2,0,0,1,2,1]
print(confusion_matrix(y_true, y_pred))

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
print(confusion_matrix(y_true, y_pred, labels=['ant', 'bird', 'cat']))
'''
    ant bird cat
ant  2   0    0
bird 0   0    1
cat  1   0    2
'''

y_true =[0,0,1,0]
y_pred = [1,0,1,0]
# y_true=[2,1,0,1,2,0]
# y_pred=[2,0,0,1,2,1]
# 准确率 (TP+TN) / (TP+FP+TN+FN)
print('-------------准确率---------------')
from sklearn.metrics import accuracy_score
print(confusion_matrix(y_true, y_pred))
print(accuracy_score(y_true, y_pred))

# 精确率 TP / (TP+FP) 表示正确分类的正例(分类为1)个数占分类(预测)为正例的实例个数的比例
print('-------------精确率---------------')
from sklearn.metrics import precision_score
print(confusion_matrix(y_true, y_pred))
print(precision_score(y_true, y_pred))

# 召回率 TP / (TP+FN) 指分类器分类正确的正样本个数占所有的正样本个数的比例。
print('-------------召回率---------------')
from sklearn.metrics import recall_score
print(confusion_matrix(y_true, y_pred))
print(recall_score(y_true, y_pred, average='macro'))

# classification_report 函数用于显示主要分类指标的文本报告．在报告中显示每个类的精确度，召回率，F1值等信息
print('-------------classification_report---------------')
from sklearn.metrics import classification_report
y_true =[0,0,1,0]
y_pred = [1,0,1,0]
target_names = ['class 0', 'class 1']
report = classification_report(y_true, y_pred, target_names=target_names)
print(report)