#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from alipay import AliPay

APP_ID = '2016091800548041'
PRIVATE_KEY = open('app_private_key.pem').read()
ALIPAY_PUBLIC_KEY = open('alipay_public_key.pem').read()

# 初始化Alipay对象
alipay = AliPay(
    appid=APP_ID,
    app_notify_url=None,  # 默认回调url
    app_private_key_string=PRIVATE_KEY,
    alipay_public_key_string=ALIPAY_PUBLIC_KEY,
    sign_type='RSA2',  # RSA2或RSA
    debug=False  # 默认False
)

# 构造请求参数
biz_content = {
    'out_trade_no': '20150320010101001',  # 商户订单号
    'total_amount': '88.88',  # 订单总金额
    'subject': 'Iphone6 16G',  # 订单标题
    'product_code': 'FAST_INSTANT_TRADE_PAY',  # 销售产品码
}

# 发起支付请求
result = alipay.api_alipay_trade_page_pay(
    out_trade_no=biz_content['out_trade_no'],
    total_amount=biz_content['total_amount'],
    subject=biz_content['subject'],
    product_code=biz_content['product_code'],
    return_url='http://www.example.com',  # 支付完成后跳转的URL
)

# 处理响应结果
if result['code'] == '10000' and alipay.verify(result, result['sign']):
    # 支付请求成功且验签通过，获取支付宝交易号
    trade_no = result['trade_no']
    # TODO: 处理业务逻辑
else:
    # 支付请求失败或验签失败，打印错误信息
    print(result['msg'])