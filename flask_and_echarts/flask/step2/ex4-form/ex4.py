from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('ex4.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      res = request.form
      return render_template("result.html",result = res)

if __name__ == '__main__':
   app.run(debug = True)