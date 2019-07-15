import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    # 从csv中读取有用的信息
    df = pd.read_csv('data.csv')
    # 空值填0
    df = df.fillna(0)
    # (4000, 59)
    array = np.array(df)
    # (4000, 57)
    x = array[:, 1:-1]
    # scale
    x[:, -1] /= np.mean(x[:, -1])
    x[:, -2] /= np.mean(x[:, -2])
    # (4000, )
    y = array[:, -1]

    # 划分训练集与验证集
    x_train, x_val = x[0:3500, :], x[3500:4000, :]
    y_train, y_val = y[0:3500], y[3500:4000]

    classifier = LogisticRegression()
    classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_val)
    print(predictions)

    for i in enumerate(predictions[-5:]):
        print('预测：%d' % int(i[1]))

    print(accuracy_score(y_val, predictions))

if __name__ == '__main__':
    main()