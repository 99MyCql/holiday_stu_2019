from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
""" 转换器构建规则
int   接受整数
float  对于浮点值
path   接受用作目录分隔符的斜杠

"""

@app.route('/post/<float:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %f' % post_id


if __name__ == '__main__':
    app.run()