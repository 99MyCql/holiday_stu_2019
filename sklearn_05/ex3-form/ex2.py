from flask import Flask, render_template, request, redirect, url_for

from sklearn.externals import joblib

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('ex2.html')

@app.route('/pause')
def pause():
    return 'pause'

@app.route('/predict', methods=['post'])#装饰器
def predict():
    # 如果不是post方法，则重定向到index页面
    print(request.method)
    if request.method != 'POST':
        print('hello')
        return redirect(url_for('index'))
    sepalLength = request.form.get('sepalLength')
    sepalWidth = request.form.get('sepalWidth')
    petalLength = request.form.get('petalLength')
    petalWidth = request.form.get('petalWidth')
    X = [[float(sepalLength), float(sepalWidth), float(petalLength), float(petalWidth)]]#二维数组，构成X的特征
    clf = joblib.load('iris_lr_model.pkl')
    probabilities = clf.predict_proba(X)

    # print('hello')
    res = {
        'Iris-Setosa': round(probabilities[0, 0] * 100, 2),
        'Iris-Versicolour': round(probabilities[0, 1] * 100, 2),
        'Iris-Virginica': round(probabilities[0, 2] * 100, 2)
        }
    return render_template("result.html",result = res)#传入字典,result会解析res，传给页面


if __name__ == '__main__':
    app.run(debug=True)
