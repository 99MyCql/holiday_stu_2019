#coding:utf-8
from flask import render_template
from flask import Flask, url_for

app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    #渲染template目录下的hello.html
    return render_template('ex2.html', name=name)

if __name__ == '__main__':
    app.debug = True  # 作用是修改完文件，服务器自动重启
    app.run(host = '0.0.0.0')
