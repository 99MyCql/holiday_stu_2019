from flask import Flask, render_template, request,redirect

from sklearn.externals import joblib

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('ex2.html')

@app.route('/pause')
def pause():
    return 'pause'

@app.route('/predict')
def predict():
    return 'predict'

if __name__ == '__main__':
    app.run(debug=True)
