from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

def hello2fn():
   return 'hello world,hello world'
app.add_url_rule('/hello2', 'hello2', hello2fn)

if __name__ == '__main__':
    app.run()