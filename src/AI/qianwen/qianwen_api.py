from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-056307bb19274ce5b486109e2993c9a0"

import requests

# 使用您的AccessKey ID和AccessKey Secret
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'

# DashScope灵积模型服务的地址
api_url = 'https://dashscope.aliyun.com/api/'

# 初始化会话参数
session_params = {
    'service': 'qianwen',
    'model':   'large',  # 模型大小选择，如：small, large等
    'project': 'default_project',  # 默认项目名称
    'scene':   'default_scene'  # 默认场景名称
}

# 发起会话请求
headers = {'Authorization': f'acs {access_key_id}:{access_key_secret}'}
response = requests.post(api_url + 'sessions', json=session_params, headers=headers)
if response.status_code != 200:
    print(f"Error starting session: {response.text}")
else:
    session_id = response.json()['session_id']

# 开始对话
while True:
    user_input = input("User: ")

    # 向服务器发送请求
    message_params = {
        'session_id': session_id,
        'text':       user_input
    }
    response = requests.post(api_url + 'messages', json=message_params, headers=headers)
    if response.status_code != 200:
        print(f"Error sending message: {response.text}")
    else:
        print(f"QianWen: {response.json()['answer']['text']}")