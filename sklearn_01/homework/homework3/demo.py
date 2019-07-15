import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    df = pd.read_csv('data.csv')
    print(df.columns)
    nj_df = df[df['city'] == '南京市']
    print(len(nj_df.index))

    x = []
    y = []
    for i in range(int(len(nj_df.index) / 24)):
        for j in range(24-8):
            temp = []
            for k in range(8):
                temp.append(nj_df.iloc[i+j+k, 2])
            x.append(temp)
            y.append(nj_df.iloc[i+j+8, 2])

    x = np.array(x).astype(float)
    y = np.array(y).astype(float)
    print(x)
    print(y)
    print(len(x))

    #划分训练集与验证集
    x_train, y_train = x[0:100], y[0:100]
    x_val, y_val = x[100:-1], y[100:-1]

    # 训练
    model = LinearRegression()
    model.fit(x_train, y_train)

    # 预测
    for i in range(len(x_val)):
        print('predict: %f, validate: %f' % (model.predict([x_val[i]]), y_val[i]))

    # 评分
    print('the score is: %.6f' % model.score(x_val, y_val))

if __name__ == '__main__':
    main()