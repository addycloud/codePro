#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""

"""
import json

import requests
from bs4 import BeautifulSoup

from src.utils.file_util import read_file, write_to_file


def login():
    path = r"../common/config.yaml"
    login_data = read_file(path)["leetCode"]
    print("=====login_data===", login_data)
    # 登录的用户名和密码
    username = login_data["user"]
    password = login_data["pwd"]
    # 登录页面的 URL 和登录请求的 URL
    login_url = "https://leetcode.com/accounts/login/"
    do_login_url = "https://leetcode.com/accounts/login/?next=/problems/"

    # 创建一个会话
    session = requests.Session()
    print("====session====", session)

    # 访问登录页面，获取 csrf_token 和 cookies
    response = session.get(login_url)
    # print("====response====", response)
    soup = BeautifulSoup(response.text, "html.parser")
    # print("====soup====", soup)
    cookies = response.cookies.get_dict()

    # csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
    # # 构造登录请求的数据
    # data = {
    #     "csrfmiddlewaretoken": csrf_token,
    #     "login": username,
    #     "password": password,
    #     "next": "/problems/",
    # }
    #
    # # 发送登录请求
    # response = session.post(do_login_url, data=data, cookies=cookies)
    # print("====response====", response)
    return cookies


def get_all_problem():
    url = "https://leetcode.com/api/problems/all/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        problems = data['stat_status_pairs']
        # print("====problems:{}".format(problems))
        write_to_file("../common/test.json", problems)

        # for problem in problems:
        #     if problem['difficulty']['level'] == 1:  # 只输出难度为简单的问题
        #         print(problem['stat']['question__title'])
    else:
        print("Failed to get problem data from LeetCode API")


def get_topic(session):
    # 获取题目页面的 HTML
    response = session.get("https://leetcode.com/problemset/all/")
    soup = BeautifulSoup(response.text, "html.parser")

    # 解析 HTML，获取题目列表
    problem_list = soup.find_all("div", {"class": "reactable-data"})

    for problem in problem_list:
        problem_id = problem.find("a", {"class": "ac"}).string
        problem_title = problem.find("a", {"class": "reactable-toggle"}).string
        print(f"{problem_id}\t{problem_title}")


def get_first(cookie):
    # 设置LeetCode API的URL和查询参数
    url = 'https://leetcode-cn.com/api/problems/all/'
    params = {'limit': '1'}

    # 设置请求头，添加用户信息
    headers = {
        'Cookie': '{}'.format(cookie)
    }

    # 发送HTTP GET请求，获取题库信息
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    # 从响应中提取第一道题的信息
    problems = json.loads(response.text)['stat_status_pairs']
    write_to_file("../common/test.json", problems)
    if len(problems) > 0:
        problem = problems[0]['stat']
        print("====problem:{}".format(problem))
        print("题目标题：{}".format(problem['question__title']))
        print("题目信息：")
        print("  难度等级：{}".format(problem['difficulty']['level']))
        print("  通过率：{:.2f}%".format(problem['total_acs'] / problem['total_submitted'] * 100))
        print("  问题描述：{}".format(problem['translatedContent']))
    else:
        print("题库中没有题目！")


if __name__ == '__main__':
    # login()
    # get_all_problem()
    get_first(login())
