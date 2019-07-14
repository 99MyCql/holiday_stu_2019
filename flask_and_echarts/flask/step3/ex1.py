from flask import Flask, jsonify

app = Flask(__name__)

json_data = [
  {"name":"json", "age":123} 
]

@app.route('/jsontest', methods=['GET'])
def get_json():
  return jsonify({'data': json_data})

app.run()