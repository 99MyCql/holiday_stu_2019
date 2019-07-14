# Flask表单 

'''
目的：实现一个简单的登陆的逻辑处理
1.路由需要有get和post两种请求方式 --> 需要判断请求方式
2.获取请求的参数（从表单中拿到数据）
3.判断参数是否填写，以及密码是否相同
4.如果判断都没有问题，就返回一个success
'''

'''
给模板传递消息
flash --> 需要对内容加密，因此需要设置secret_key，做加密消息的混淆
模板中需要遍历flash消息
'''

from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'itheima'

@app.route('/', methods=['GET','POST'])
def index():

    #request：请求对象 --> 获取请求方式、数据
    #1. 判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数 request(通过input中的name值)
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        print(username,password,password2)

        # 3.判断参数是否填写&密码是否相同(u是为了解决编码问题)
        if not all([username,password,password2]):
            # print('参数不完整')
            flash(u'参数不完整')
        elif password != password2:
            # print('密码不一致')
            flash(u'密码不一致')
        else:
            return  'success'

    return render_template('ex3.html')

if __name__ == '__main__':
    app.run(debug=True)