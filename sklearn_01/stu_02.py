'''
逻辑回归。一件事情只有0、1两种结果，根据训练模型从而对问题判断0、1
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('mlslpic/SMSSpamCollection', delimiter='\t', header=None)
print(df.head())

# train_test_split() 分成训练集（75%）和测试集（25%）
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1], df[0])
print(X_train_raw.head())
print(y_train.head())

# 建一个TfidfVectorizer实例来计算TF-IDF权重
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)
X_test = vectorizer.transform(X_test_raw)
print(X_train)
print(X_test)

classifier = LogisticRegression() # 建立逻辑回归模型
classifier.fit(X_train, y_train) # 训练模型
predictions = classifier.predict(X_test) # 预测

for i, prediction in enumerate(predictions[-5:]):
    print('预测类型：%s. 信息：%s' % (prediction, X_test_raw.iloc[i]))

print(accuracy_score(y_test, predictions)) # 评估