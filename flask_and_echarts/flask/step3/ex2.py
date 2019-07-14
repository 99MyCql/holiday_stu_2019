from flask import Flask
from flask import jsonify
from flask import Response
 
 
app = Flask(__name__)
 
 
@app.route('/hello/<name>/<words>',methods=['GET'])
def hello(name,words):
    return jsonify({'name':name,'words':words})#也可以传入key=value形式的参数，如jsonify(name=name,words=words)
 
 
if __name__ == '__main__':
    app.run()