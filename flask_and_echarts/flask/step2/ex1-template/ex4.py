from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('ex4.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)