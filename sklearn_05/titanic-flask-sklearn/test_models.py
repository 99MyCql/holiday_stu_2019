import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from prepare_data import (
    encode_variables,
    explained_var,
    explanatory_vars,
    fill_gaps
)

training_data = pd.read_csv('data/train.csv')
fill_gaps(training_data)
encode_variables(training_data)
num_test = 0.20
X_all = training_data[explanatory_vars]
y_all = training_data[explained_var]
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=23)


# don't let our pickled model get working worse
# than we train and adjust them to work


def test_model_random_forest_has_expected_accuracy_or_better():
    rf = joblib.load('models/random_forest.pkl')
    predictions = rf.predict(X_test)
    assert accuracy_score(y_test, predictions) >= 0.7932960893854749


def test_model_logistic_regression_has_expected_accuracy_or_better():
    lr = joblib.load('models/logistic_regression.pkl')
    predictions = lr.predict(X_test)
    assert accuracy_score(y_test, predictions) >= 0.7877094972067039


def test_model_knn_has_expected_accuracy_or_better():
    knn = joblib.load('models/knn.pkl')
    predictions = knn.predict(X_test)
    assert accuracy_score(y_test, predictions) >= 0.7262569832402235
