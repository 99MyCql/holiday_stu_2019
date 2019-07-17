import numpy as np
from sklearn.ensemble import AdaBoostClassifier # AdaBoost 分类
from sklearn.tree import DecisionTreeClassifier # 决策树分类
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import GridSearchCV # 网格搜索

# 生成2维正态分布，生成的数据按分位数分为两类，500个样本,2个样本特征，协方差系数为2
X1, y1 = make_gaussian_quantiles(cov=2.0,n_samples=500, n_features=2,n_classes=2, random_state=1)
# 生成2维正态分布，生成的数据按分位数分为两类，400个样本,2个样本特征均值都为3，协方差系数为2
X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,n_samples=400, n_features=2, n_classes=2, random_state=1)
#讲两组数据合成一组数据
X = np.concatenate((X1, X2))
y = np.concatenate((y1, - y2 + 1))

# 随机参数传递
abd_clf = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
    algorithm="SAMME",
    n_estimators=200,
    learning_rate=0.8)
abd_clf.fit(X, y)
print("Score: %.6f" % abd_clf.score(X,y))

# 参数网格调优
param_grid = {
    'base_estimator': [DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5)],
    'algorithm': ['SAMME'],
    'n_estimators': list(range(100, 500, 100)),
    'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
}

# 观察角度分别有准度与回归
scores = ['precision', 'recall']
adb_clf = AdaBoostClassifier()
for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    grid = GridSearchCV(adb_clf, param_grid, cv=5, scoring='%s_macro' % score)
    grid.fit(X, y)
    print('网格搜索-最佳度量值:', grid.best_score_) # 获取最佳度量值
    print('网格搜索-最佳参数:', grid.best_params_) # 获取最佳度量值时的代定参数的值。是一个字典
    print('网格搜索-最佳模型:', grid.best_estimator_) # 获取最佳度量时的分类器模型