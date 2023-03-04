# -*- coding: UTF-8 -*-
# coding=utf-8

from east_money import get_client
from src.utils.file_util import read_file

# pip install pycryptodome
# 使用前先删除当前目录的validateKey.txt和cookie.txt文件

if __name__ == '__main__':
    path = r"../../common/config.yaml"
    login_data = read_file(path)["east"]
    # isOcr: false 运行后, 查看当前目录生成的yzm.png, 手动输入验证码, true 自动识别验证码, 需要配置阿里云appcode
    client = get_client(login_data["user"], login_data["pwd"], isOcr=False)
    print("test")
    # 只要登录一次, 登录后 cookie 存在本地文件, 过期后需要重新登录
    # client.login()
    #
    # r = client.get_stock_list()
    # print(r)
    #
    # r = client.get_assets()
    # print(r)
    #
    # r = client.submit('200', '33.02', 'S', '300059', '东方财富')
    # print(r)
