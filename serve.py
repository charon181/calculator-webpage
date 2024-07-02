from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    try:
        result = eval(expression)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(result=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
