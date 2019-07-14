from flask import render_template
from flask import Flask, url_for


app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('ex3.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)