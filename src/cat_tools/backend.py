#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random

from flask import Flask, render_template, request, jsonify
import requests
import urllib.parse

# from noun_dictionary import NounList
# 启动方式
app = Flask(__name__, template_folder='.')
NounList = ["2023热点", "2023新闻", "news", "study", "科技", "科学", "科学技术", "科学研究",
            "科学发展", "科学家", "科学院", "科学家", "科学家", "科学家", "科学家",
            "金融", "互联网", "web3", "AI", "人工智能", "区块链", "比特币", "以太坊", "数字"
            ]
DEFAULT_KEY_WORD = random.choice(NounList)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    try:
        print(f"request.json: {request.json}", flush=True)
        print(f"request.form: {request.form}", flush=True)
        # print(f"request.form['keyWord']: {request, type(request), request.json}", flush=True)
        key_word = request.json.get("json").get("keyWord") if request.json else DEFAULT_KEY_WORD
        print(f"keyWord: {key_word}")

        json_data = {
            'keyWord': urllib.parse.quote(key_word)
        }
        print(f"json_data: {json_data}")
        response = requests.post('https://tool.browser.qq.com/api/searchPdf', headers=headers, json=json_data)
        result = response.json()
        print(f"result: {result}")
        return jsonify(result)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    app.run(debug=True)
