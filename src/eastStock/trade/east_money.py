# -*- coding: UTF-8 -*-
# coding=utf-8

import time
import random
import requests
import json
import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

"""
get_asserts https://jywg.18.cn/Com/queryAssetAndPositionV1?validatekey=${validatekey}   我的资产
submit  https://jywg.18.cn/Trade/SubmitTradeV2?validatekey=${validatekey}   提交挂单
revoke  https://jywg.18.cn/Trade/RevokeOrders?validatekey=${validatekey}    撤单
get_stock_list  https://jywg.18.cn/Search/GetStockList?validatekey=${validatekey}   我的持仓
get_orders_data https://jywg.18.cn/Search/GetOrdersData?validatekey=${validatekey}  当日委托
get_deal_data   https://jywg.18.cn/Search/GetDealData?validatekey=${validatekey}    当日成交
get_his_deal_data   https://jywg.18.cn/Search/GetHisDealData?validatekey=${validatekey} 历史成交
get_his_orders_data https://jywg.18.cn/Search/GetHisOrdersData?validatekey=${validatekey}   历史委托
get_can_buy_new_stock_list_v3   https://jywg.18.cn/Trade/GetCanBuyNewStockListV3?validatekey=${validatekey} 查询可申购新股列表
get_convertible_bond_list_v2    https://jywg.18.cn/Trade/GetConvertibleBondListV2?validatekey=${validatekey}    查询可申购新债列表
submit_bat_trade_v2 https://jywg.18.cn/Trade/SubmitBatTradeV2?validatekey=${validatekey}    批量申购
"""


def dlog(*s):
    template = '{}'
    for arg in s:
        template = template + ' {}'

    print(template.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *s))
    return


def rsa_encrypt(msg):
    public_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDHdsyxT66pDG4p73yope7jxA92\nc0AT4qIJ/xtbBcHkFPK77upnsfDTJiVEuQDH+MiMeb+XhCLNKZGp0yaUU6GlxZdp\n+nLW8b7Kmijr3iepaDhcbVTsYBWchaWUXauj9Lrhz58/6AE/NF0aMolxIGpsi+ST\n2hSHPu3GSXMdhPCkWQIDAQAB
-----END PUBLIC KEY-----'''
    pub_obj = RSA.importKey(public_key)
    cipher = Cipher_pkcs1_v1_5.new(pub_obj)
    msg = cipher.encrypt(msg.encode())
    return base64.b64encode(msg).decode("utf-8")


class EastMoneyClient:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/48.0.2564.109 Safari/537.36'
    }

    def __init__(self, accountId, password, isOcr=False):
        self.accountId = accountId
        self.password = password
        self.session = requests.Session()
        self.isOcr = isOcr

        self.__loadCookie()

    def __loadCookie(self):
        cookie_path = '../cache/cookie.txt'
        if os.path.isfile(cookie_path):
            with open(cookie_path, 'r') as f:
                try:
                    self.session.cookies.update(json.loads(f.read()))
                except ValueError:
                    pass

        key_path = "../cache/validateKey.txt"
        if os.path.isfile(key_path):
            with open(key_path, 'r') as f:
                self.validateKey = f.read()

    def __ocr(self, filename):
        # https://market.aliyun.com/products/57124001/cmapi027426.html#sku=yuncode2142600000
        appcode = ''
        with open(filename, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/48.0.2564.109 Safari/537.36',
                'Authorization': 'APPCODE ' + appcode}
            params = {"image": base64_data, "type": "1003"}

            r = requests.post('https://302307.market.alicloudapi.com/ocr/captcha', data=params, headers=headers)
            dlog(r)
            j = r.json()
            dlog(j)
            return j['data']['captcha']

    def login(self):
        times = 0
        while times < 3:
            randNumber = '0.903' + str(int(time.time()) * 1000 + random.randint(0, 1000))

            content = requests.get(url='https://jywg.18.cn/Login/YZM?randNum=' + randNumber,
                                   headers=self.headers).content
            with open('yzm.png', 'wb') as f:
                f.write(content)

            if self.isOcr:
                identifycode = self.__ocr('yzm.png')
            else:
                identifycode = input('yzm.png, input captcha: ')
            params = {
                'userId': self.accountId,
                'password': self.password,
                'duration': 1800,
                'type': "Z",
                'randNumber': randNumber,
                'identifyCode': identifycode
            }

            dlog(params)

            headers = dict(self.headers)
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, ' \
                                'like Gecko) Chrome/106.0.0.0 Safari/536.66'

            response = self.session.post('https://jywg.18.cn/Login/Authentication', data=params, headers=headers)

            dlog(response.status_code)
            print(response.text)

            if response.status_code == 200:
                data = json.loads(response.text)
                if data.get('Status') == 0:
                    with open('../cache/cookie.txt', 'w') as f:
                        f.write(json.dumps(self.session.cookies.get_dict()))

                    r = self.session.get('https://jywg.18.cn/Trade/Buy', headers=self.headers)
                    self.validateKey = r.text.split('em_validatekey', 1)[1].split('value="')[1].split('"')[0]
                    with open('../cache/validateKey.txt', 'w') as f:
                        f.write(self.validateKey)

                    dlog('login success')
                    break

            times = times + 1

        if times >= 3:
            print('login fail')
            exit(1)
        return

    def get_assets(self):
        params = {
        }
        r = self.session.post('https://jywg.18.cn/Com/queryAssetAndPositionV1?validatekey=' + self.validateKey,
                              data=params, headers=self.headers)
        return r.text

    def submit(self, amount, price, tradetype, stockcode, zqmc):
        params = {
            'amount': amount,
            'price': price,
            'tradeType': tradetype,
            'stockCode': stockcode,
            'zqmc': zqmc
        }
        r = self.session.post('https://jywg.18.cn/Trade/SubmitTradeV2?validatekey=' + self.validateKey, data=params,
                              headers=self.headers)
        return r.text

    def get_stock_list(self):
        params = {
        }
        r = self.session.post('https://jywg.18.cn/Search/GetStockList?validatekey=' + self.validateKey, data=params,
                              headers=self.headers)
        return r.text

    def get_orders(self):
        params = {}
        r = self.session.post('https://jywg.18.cn/Search/GetOrdersData?validatekey=' + self.validateKey, data=params,
                              headers=self.headers)
        return r.text

    def revoke(self):
        # https://jywg.18.cn/Trade/RevokeOrders?validatekey='+self.validateKey
        params = {'revokes': '20220212_委托编号'}
        return


def get_client(accountId, _password, isOcr=False):
    # if len(password) <= 20:
    password = rsa_encrypt(_password)
    client = EastMoneyClient(accountId, password, isOcr)
    print("====client:{}".format(client))
    return client
