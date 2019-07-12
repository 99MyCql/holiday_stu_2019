'''
国内祁总公司
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv('unicorn_china.csv')
print(df.info())
print(df.columns)

print(df['Industry'].value_counts())
print(df['Select Investors'].head(3))
print(df['Select Investors'].str.split('、').head(3))
print(df['Select Investors'].str.split('、', expand=True).apply(pd.Series).head(3))
newdf = df['Select Investors'].str.split('、', expand=True).apply(pd.Series)
print(newdf.head(3))
print(newdf.apply(pd.value_counts).fillna(0))
newdf2 = newdf.apply(pd.value_counts).fillna(0)
print(newdf2.sum(axis=1).astype('int').sort_values(ascending=False))