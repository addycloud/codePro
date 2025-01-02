from flask import Flask, request, jsonify, render_template
from http import HTTPStatus
import dashscope

app = Flask(__name__)
dashscope.api_key = "sk-056307bb19274ce5b486109e2993c9a0"



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tokenizer', methods=['POST'])
def tokenizer():
    data = request.get_json()
    messages = data.get('messages', [])

    response = dashscope.Tokenization.call(model='qwen-turbo', messages=messages)

    if response.status_code == HTTPStatus.OK:
        result = response.json().get('result', '')
        return jsonify(result=result), HTTPStatus.OK
    else:
        return jsonify(error='请求失败'), HTTPStatus.INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(debug=True)
