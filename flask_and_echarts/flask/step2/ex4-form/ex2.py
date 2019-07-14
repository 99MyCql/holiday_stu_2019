from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('ex2.html')
 
@app.route('/login', methods=['post'])
def login():
	# request.form['name]  字典或get方法
    name = request.form.get('name')
    password = request.form.get('password')
    if name == 'admin' and password == '123':
        return render_template('ex2.html', name=name)
    # 输入错误密码，重新输入
    return render_template('ex2.html')
 
# @app.route('/login', methods=['get', 'post'])
# def login():
#     name = request.form.get('name')
#     password = request.form.get('password')
#     if name == 'admin' and password == '123':
#         return redirect(url_for('login'))  # 重定向
#     return render_template('ex2.html')


if __name__ == '__main__':
    app.run(debug=True)

