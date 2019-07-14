# coding:utf-8

from __future__ import unicode_literals

from flask import Flask,render_template,jsonify, redirect

#生成Flask实例
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return redirect("/combine")

@app.route('/combine')
def combine():
    return render_template('combine.html')


@app.route('/bar')
def bar_echart():

    return render_template('bar.html')


@app.route('/list')
def list_echart():
    return render_template('list.html')

@app.route('/pie')
def pie_echart():

    return render_template('pie.html')


@app.route('/barAjax')
def bar_ajax_echart():

    return render_template('barAjax.html')

@app.route('/barApi')
def pie_echart_api():

    return jsonify({
         'name': [u"衬衫",u"羊毛衫",u"雪纺衫",u"裤子",u"高跟鞋",u"袜子"],
         'data': [5, 20, 36, 10, 10, 20]
     })


@app.route('/listAjax')
def list_ajax_echart():

    return render_template('listAjax.html')


@app.route('/listApi')
def list_echart_api():

    return jsonify({
         'legend': [u'邮件营销',u'联盟广告',u'视频广告',u'直接访问',u'搜索引擎'],
         'xAxis': [u'周一',u'周二',u'周三',u'周四',u'周五',u'周六',u'周日'],
         'data_list' : [[120, 132, 101, 134, 90, 230, 210],
                        [220, 182, 191, 234, 290, 330, 310],
                        [150, 232, 201, 154, 190, 330, 410],
                        [320, 332, 301, 334, 390, 330, 320],
                        [820, 932, 901, 934, 1290, 1330, 1320]
                     ]
     })


if __name__ == "__main__":
    #运行项目
    app.run(app.run(debug=True, port=5000, host='0.0.0.0'))
