from flask import Flask,render_template,url_for, jsonify

import json

#生成Flask实例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# json.dumps()解决同样的问题可以加入ensure_ascii=False

@app.route('/')
def my_echart():
    #在浏览器上渲染模板
    return render_template('sample3.html')

# /data路由接收前端的ajax请求
@app.route('/data',methods=['GET'])
def my_echart_data():
    # 读取json文件（如果是从数据库中获取，那么前面还需添加一部分代码以从数据库中取出数据，用到import sqlite3或pymysql）
    with open("data.json","r",encoding='UTF-8') as f:
        load_json = json.load(f)
    # 将其转换为Jason格式
    return jsonify(load_json)
    

if __name__ == "__main__":
    #运行项目
    app.run(debug = True)