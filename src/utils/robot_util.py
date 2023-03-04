#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""

"""
import requests
import json
from src.utils.file_util import read_file


def push_robot(_url, _date):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "[push]{}".format(_date)
        }
    }

    response = requests.post(_url, headers=headers, data=json.dumps(data))
    print(response.text)


if __name__ == '__main__':
    test_str = "test_str"
    path = r"..\common\config.yaml"
    url = read_file(path)["ddRobot"]
    push_robot(url, test_str)
