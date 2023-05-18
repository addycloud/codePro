#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests


def post_commit():
    import requests

    headers = {
        'authority':          'plausible.midway.run',
        'accept':             '*/*',
        'accept-language':    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type':       'text/plain',
        'origin':             'chrome-extension://iaakpnchhognanibcahlpcplchdfmgma',
        'sec-ch-ua':          '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile':   '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest':     'empty',
        'sec-fetch-mode':     'cors',
        'sec-fetch-site':     'cross-site',
        'user-agent':         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
    }

    data = '{"n":"send_message","u":"chrome-extension://iaakpnchhognanibcahlpcplchdfmgma/app.html#/chat/bing","d":"chathub.gg","r":null,"w":1177,"h":1,"p":"{\\"botId\\":\\"bing\\"}"}'

    response = requests.post('https://plausible.midway.run/api/event', headers=headers, data=data)
    return response


def main():
    response = post_commit()
    # 获取事件内容
    events = response.content

    # 打印事件内容
    print(events)


if __name__ == '__main__':
    main()
