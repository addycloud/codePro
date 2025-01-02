import requests

# 设置 API Key 和请求头
API_KEY = ""
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
}

# 初始化对话历史
messages = [
    {
        "role":    "system",
        "content": "You are a helpful assistant."
    }
]


def chat_with_deepseek():
    print("Welcome to the DeepSeek Chat! Type 'exit' to end the conversation.")
    while True:
        # 获取用户输入
        user_input = input("You: ")

        # 如果用户输入 'exit'，则退出对话
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # 将用户输入添加到对话历史中
        messages.append({"role": "user", "content": user_input})

        # 构建请求数据
        json_data = {
            'model':    'deepseek-chat',
            'messages': messages,
            'stream':   False,  # 关闭流式响应
        }

        try:
            # 调用 DeepSeek API
            response = requests.post(
                'https://api.deepseek.com/chat/completions',
                headers=HEADERS,
                json=json_data
            )
            response.raise_for_status()  # 检查请求是否成功

            # 提取助手的回复
            assistant_reply = response.json()['choices'][0]['message']['content']
            print(f"DeepSeek: {assistant_reply}")

            # 将助手的回复添加到对话历史中
            messages.append({"role": "assistant", "content": assistant_reply})
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


# 启动对话
chat_with_deepseek()