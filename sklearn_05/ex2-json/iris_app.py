from flask import Flask, jsonify, request
import os
from sklearn.externals import joblib


app = Flask(__name__)

# index page
@app.route('/')
def index():
	return 'Index Page'

# hello world page
@app.route('/hello')
def hello():
	return 'Hello World!'

@app.route("/predict", methods=['POST'])
def predict():
    # get iris object from request
    X = request.get_json()
    # parse data into a float
    X = [[float(X['sepalLength']), float(X['sepalWidth']), float(X['petalLength']), float(X['petalWidth'])]]

    # read model. load your particular model by its .pkl file name
    # clf = 'classifier'
    clf = joblib.load('iris_lr_model.pkl')
    # pass parsed variables into the model. in this case we will get probabilities in return
    probabilities = clf.predict_proba(X)

    #call the [jasonify] method of Flask to send the response data as JSON
    return jsonify([{'name': 'Iris-Setosa', 'value': round(probabilities[0, 0] * 100, 2)},
                    {'name': 'Iris-Versicolour', 'value': round(probabilities[0, 1] * 100, 2)},
                    {'name': 'Iris-Virginica', 'value': round(probabilities[0, 2] * 100, 2)}])      


if __name__ == '__main__':
    app.run(debug=True)