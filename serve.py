import time
import requests
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

REQUEST_URL = 'https://charon181.github.io/calculator-webpage/request.json'
RESULT_URL = 'https://charon181.github.io/calculator-webpage/result.json'

@app.route('/result', methods=['GET'])
def get_result():
    try:
        with open('result.json', 'r') as f:
            result_data = json.load(f)
        return jsonify(result=result_data)
    except Exception as e:
        return jsonify(result=str(e))

def fetch_request():
    try:
        response = requests.get(REQUEST_URL)
        if response.status_code == 200:
            data = response.json()
            return data.get('expression')
    except Exception as e:
        print(f"Error fetching request: {e}")
    return None

def update_result(result):
    try:
        with open('result.json', 'w') as f:
            json.dump({"result": result}, f)
        # Optionally update the GitHub Pages with the result
        # response = requests.put(RESULT_URL, json={"result": result})
    except Exception as e:
        print(f"Error updating result: {e}")

def calculate_expression(expression):
    try:
        result = eval(expression)
    except Exception as e:
        result = str(e)
    return result

def process_requests():
    while True:
        expression = fetch_request()
        if expression:
            result = calculate_expression(expression)
            update_result(result)
        time.sleep(0.5)

if __name__ == '__main__':
    from threading import Thread

    def run_app():
        app.run(host='0.0.0.0', port=8002)

    Thread(target=run_app).start()
    Thread(target=process_requests).start()


