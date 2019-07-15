import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 数据预处理
def dataProcess(df):
    x_list, y_list = [], []
    # df替换指定元素，将空数据填充为0
    df = df.replace(['NR'], [0.0])
    # astype() 转换array中元素数据类型
    array = np.array(df).astype(float)
    # 将数据集拆分为多个数据帧
    for i in range(0, 4320, 18):
        for j in range(24-9):
            mat = array[i:i+18, j:j+9]
            label = array[i+9, j+9] # 第10行是PM2.5
            x_list.append(mat)
            y_list.append(label)
    x = np.array(x_list)
    y = np.array(y_list)
    return x, y, array

def main():
    df = pd.read_csv('data.csv', usecols=range(3,27))
    # print(df)
    # print(df.columns)

    # 数据预处理
    x, y, _ = dataProcess(df)
    print(x.shape)

    # 数据再处理
    new_x = []
    for i in range(len(x)):
        temp = []
        for j in range(len(x[i])):
            for k in range(len(x[i][j])):
                temp.append(x[i][j][k])
        new_x.append(temp)

    new_x = np.array(new_x)
    print(new_x.shape)

    #划分训练集与验证集
    x_train, y_train = new_x[0:3200], y[0:3200]
    x_val, y_val = new_x[3200:3600], y[3200:3600]

    # 训练
    model = LinearRegression()
    model.fit(x_train, y_train)

    # 预测
    for i in range(len(x_val)):
        print('predict: %.6f, validate: %.6f' % (model.predict([x_val[i]]), y_val[i]))

    # 评分
    print('the score is: %.6f' % model.score(x_val, y_val))

if __name__ == '__main__':
    main()