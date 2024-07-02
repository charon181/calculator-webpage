from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 存储请求和结果
request_data = None
result_data = None

@app.route('/submit', methods=['POST'])
def submit_expression():
    global request_data
    data = request.get_json()
    request_data = data['expression']
    return jsonify(status="submitted")

@app.route('/result', methods=['GET'])
def get_result():
    global result_data
    return jsonify(result=result_data)

def calculate_expression():
    global request_data, result_data
    if request_data:
        try:
            result_data = eval(request_data)
        except Exception as e:
            result_data = str(e)
        request_data = None

if __name__ == '__main__':
    from threading import Thread
    import time

    def run_app():
        app.run(host='0.0.0.0', port=8002)

    def process_requests():
        while True:
            calculate_expression()
            time.sleep(0.5)

    Thread(target=run_app).start()
    Thread(target=process_requests).start()

