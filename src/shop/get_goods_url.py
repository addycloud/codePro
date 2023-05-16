#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

import requests


def get_goods_info():
    cookies = {
        '_ga':                                      'GA1.1.66989966.1682040245',
        'Hm_lvt_87f2ef1ac0ed9d4bc756544ab4ada75e':  '1682040245,1684226944',
        'Hm_lpvt_87f2ef1ac0ed9d4bc756544ab4ada75e': '1684226944',
        'CMM_A_C_ID':                               '82d959d2-f3c6-11ed-be8b-167879f8c795',
        'LOGIN-TOKEN-FORSNS-CX':                    'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg1MDY0ODE1LCJpYXQiOjE2ODI0NzI4MTUsImlkIjo5MzA3MDIxNH0.Mr76t0tlvjJ58XZsxI7sH44bHGvg9hVoESSuEsdLdjs',
        '_ga_BBZXS8H6XZ':                           'GS1.1.1684226945.9.1.1684226986.0.0.0',
    }

    headers = {
        'Accept':             'application/json, text/plain, */*',
        'Accept-Language':    'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection':         'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.1.66989966.1682040245; Hm_lvt_87f2ef1ac0ed9d4bc756544ab4ada75e=1682040245,1684226944; Hm_lpvt_87f2ef1ac0ed9d4bc756544ab4ada75e=1684226944; CMM_A_C_ID=82d959d2-f3c6-11ed-be8b-167879f8c795; LOGIN-TOKEN-FORSNS-CX=Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg1MDY0ODE1LCJpYXQiOjE2ODI0NzI4MTUsImlkIjo5MzA3MDIxNH0.Mr76t0tlvjJ58XZsxI7sH44bHGvg9hVoESSuEsdLdjs; _ga_BBZXS8H6XZ=GS1.1.1684226945.9.1.1684226986.0.0.0',
        'Origin':             'https://www.chanxuan.com',
        'Referer':            'https://www.chanxuan.com/',
        'Sec-Fetch-Dest':     'empty',
        'Sec-Fetch-Mode':     'cors',
        'Sec-Fetch-Site':     'same-site',
        'User-Agent':         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
        'X-Authorization-Cx': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg1MDY0ODE1LCJpYXQiOjE2ODI0NzI4MTUsImlkIjo5MzA3MDIxNH0.Mr76t0tlvjJ58XZsxI7sH44bHGvg9hVoESSuEsdLdjs',
        'X-Client-Id':        '170779814',
        'sec-ch-ua':          '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile':   '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-platform-id':      '10009',
    }

    params = {
        'request_id':            '00f7543247779ad409c5f7f5cac1bcfe',
        'sort_column':           'base_score',
        'day_type':              '2',
        'order_by':              'desc',
        'search_str':            '',
        'cos_ratio':             '20-',
        'free_sample_condition': '0',
        'service_guarantee':     '0',
        'shop_score':            '',
        'volume':                '',
        'shareable':             '1',
        'pv_count':              '2000-',
        'author_count':          '',
        'activity_price':        '5-50',
        'has_video':             '1',
        'has_live':              '1',
        'banner_id':             '',
        'is_free_sample':        '0',
        'cmm_cid':               '19',
        'cmm_cid_snd':           '198',
        'cmm_cid_third':         '0',
        'cmm_cid_fourth':        '0',
        'cmm_cid_fifth':         '0',
        'most_aweme_volume':     '0',
        'most_live_volume':      '0',
        'has_douyin_goods_tag':  '0',
        'is_assured':            '0',
        'has_shop_brand_tag':    '0',
        'page':                  '1',
        'size':                  '1000',
        'total_page':            '0',
    }

    response = requests.get('https://api-service.chanxuan.com/v1/home/getGoodsPage', params=params, cookies=cookies,
                            headers=headers)
    return response.json()


def main():
    goods_info = get_goods_info()
    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists('./goods.txt'):
        with open('./goods.txt', 'w') as f:
            pass

    with open('./goods.txt', 'r+') as f:
        urls = set(f.readlines())  # 读取已有的URL并去重
        for good in goods_info["data"]["list"]:
            url = good["detail_url"] + '\n'
            if url not in urls:
                f.write(url)


if __name__ == '__main__':
    main()
