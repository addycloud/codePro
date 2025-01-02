import time

import requests

from src.shop.cmm import query_link
from src.utils.file_util import read_file


def get_order(_headers, _cookies):

    cookies = _cookies

    headers = _headers

    json_data = {
        'timeRange': [
            '2022-05-18T16:00:00.000Z',
            '2023-05-18T15:59:59.999Z',
        ],
        'orderType': '',
        'skuIds': [],
        'mallIdList': [
            412061818,
        ],
        'goodsIdList': [],
        'provinceGroupId': None,
        'keywordsId': None,
        'provinceName': [],
        'othersProvinceList': [],
        'isOrderLockFontVersion': True,
        'printStatus': 0,
        'page': 1,
        'pageSize': 100,
        'confirmStartTime': 1652889600000,
        'confirmEndTime': 1684425599999,
        'sortType': 'desc',
        'sortCode': 'confirmTime',
        'isCanMerge': False,
        'isMerged': False,
        'orderLock': None,
        'refundStatusList': [
            0,
        ],
        'hideLockOrder': True,
        'hideRiskOrder': True,
    }

    response = requests.post('https://mms.pinduoduo.com/honolulu/order', cookies=cookies, headers=headers,
                             json=json_data)
    return response.json()


def decryption(_headers, _cookies):
    cookies = _cookies

    headers = _headers

    json_data = {
        'scene_code': 'order_print_undelivered',
        'order_sn': '230518-026193479213527',
        'biz_code': 'order_print',
        'receiver_info': [
            'mobile',
            'name',
            'address',
        ],
        'scene_info': {
            'id': 'N368b35cc90301192655f6c3abce11f75794b3f23f22b0d16',
        },
    }

    response = requests.post('https://mms.pinduoduo.com/fopen/order/receiver', cookies=cookies, headers=headers,
                             json=json_data)
    return response.json()


def de_1(order_sn, order_id):
    import requests

    cookies = {
        'api_uid': 'CiSJqGRFOl8+rQBzOL61Ag==',
        '_nano_fp': 'XpEJX5Pyl0dxl0XynC_zE8EFos2Hi8b0Zb4p0mIo',
        '_bee': 'EoGVDG5KRbrAhzkOqQD94A7RZlsHcHqJ',
        '_f77': '207f8428-baec-4417-9f36-fc2af35a641f',
        '_a42': 'b6b86ae2-6c3b-4eeb-a97e-58ea72e8f26f',
        'rckk': 'EoGVDG5KRbrAhzkOqQD94A7RZlsHcHqJ',
        'ru1k': '207f8428-baec-4417-9f36-fc2af35a641f',
        'ru2k': 'b6b86ae2-6c3b-4eeb-a97e-58ea72e8f26f',
        'terminalFinger': 'P7ZpiL83IIbBzyFafT2aINSkOsO4rOWk',
        'mms_b84d1838': '3500,3526,150,3523,3434,3532,3254,3474,3475,3477,3479,3482,1202,1203,1204,1205,3417,3397',
        'PASS_ID': '1-mHM6qp3cSSAUCM0E8zdgnnVl8g7z4KiEmUv51eHNV/yC776akyZwlr1FgeUiuA3stkcmMPRNr92znmQvpXRIfg_412061818_130063858',
        'x-visit-time': '1684418552924',
        'JSESSIONID': '9BB4AAB4E4BCC9E00332759007B88489',
    }

    headers = {
        'authority': 'mms.pinduoduo.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'anti-content': '0aqAfqny0jSdjgd9l0YigrZPZbZScusdMOArJjOIeg7EiIE6jncSdBgU5pQ3ct7onA7Zg--vV9Ll4ZbvBJpntvs2eB1ydL4URyCPC1FUyLLl051SfrbXaKq0JxaYYMJ6l389z0DVvjITSnNlaboiNytcNF50AkTsxSyU0mkG4gWnsVBo-ZaCFxFmgRbwAeOHNICo52GjVUNT0bqAPVNeO9Pzu7V4eeHLn24JhoapGV0FCjU5UqDH4DXUqdD1eQQDwIUzhmoIU_wwDGZaslU3A4DpDGVbGa-87faFqD33X9ZNHl22kTACYIqQ9E68OJIdpZdhMM0lKaoFbn_KqTv4ZdxbX7mfwi06QXGdV0qEFMqa3aD_VboFA6IKI57AD7rJErUWFdjuszx-zdKFZ3Di56sH2VpDgHjDgduM6G_S8iJ-KU1IybtFzFVatixYNcPhZ5pq9VlN_R7LfFV1HZZJg7xa-2ucBta0VSG9HNumDnio4YK-ZF12SJyfEm6RSi_5yRbcXmu-O9rk0aWRCv7dVwnFnh60-dheUGRcqzwBORpdyqpZeSRsdU6ZuLyQF5j3sYsUiQvEMqyFI9_J73fp7PIt3OQHU9hMQeMOIoqRSsOOj8RouJ4M5CWLKJHluAuN1a5bu-pcv_OSmpBSiBrKjI456_ZxvO0pOO5akYwQSBPO',
        'cache-control': 'max-age=0',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'api_uid=CiSJqGRFOl8+rQBzOL61Ag==; _nano_fp=XpEJX5Pyl0dxl0XynC_zE8EFos2Hi8b0Zb4p0mIo; _bee=EoGVDG5KRbrAhzkOqQD94A7RZlsHcHqJ; _f77=207f8428-baec-4417-9f36-fc2af35a641f; _a42=b6b86ae2-6c3b-4eeb-a97e-58ea72e8f26f; rckk=EoGVDG5KRbrAhzkOqQD94A7RZlsHcHqJ; ru1k=207f8428-baec-4417-9f36-fc2af35a641f; ru2k=b6b86ae2-6c3b-4eeb-a97e-58ea72e8f26f; terminalFinger=P7ZpiL83IIbBzyFafT2aINSkOsO4rOWk; mms_b84d1838=3500,3526,150,3523,3434,3532,3254,3474,3475,3477,3479,3482,1202,1203,1204,1205,3417,3397; PASS_ID=1-mHM6qp3cSSAUCM0E8zdgnnVl8g7z4KiEmUv51eHNV/yC776akyZwlr1FgeUiuA3stkcmMPRNr92znmQvpXRIfg_412061818_130063858; x-visit-time=1684418552924; JSESSIONID=9BB4AAB4E4BCC9E00332759007B88489',
        'origin': 'https://mms.pinduoduo.com',
        'platform': '1',
        'referer': 'https://mms.pinduoduo.com/print/order/list',
        'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
    }

    json_data = {
        'scene_code': 'order_print_undelivered',
        'order_sn': order_sn,  # '230518-026193479213527'
        'biz_code': 'order_print',
        'receiver_info': [
            'mobile',
            'name',
            'address',
        ],
        'scene_info': {
            'id': id,  # 'N368b35cc90301192655f6c3abce11f75794b3f23f22b0d16'
        },
    }

    response = requests.post('https://mms.pinduoduo.com/fopen/order/receiver', cookies=cookies, headers=headers,
                             json=json_data)
    print(response.text)
    # {
    #     "success": true,
    #     "error_code": 0,
    #     "result":
    #         {
    #             "order_sn": "230518-026193479213527",
    #             "virtual_mobile": "17281441316#8984",
    #             "name": "张志鹏[8984]",
    #             "address": "矣六街道华城花园5栋[8984]",
    #             "province": "云南省",
    #             "province_id": 30,
    #             "city": "昆明市",
    #             "city_id": 367,
    #             "district": "官渡区",
    #             "district_id": 3102,
    #             "show_virtual_report_button": false,
    #             "show_virtual_tip_after_mobile": false,
    #             "show_virtual_risk_tip": false,
    #             "can_virtual_extend": false,
    #             "name_pure": "张志鹏",
    #             "address_pure": "矣六街道华城花园5栋",
    #             "show_export_popup": false,
    #             "mobile_from_order_print": false
    #         }
    # }
    return response.json()


def main():
    headers = {
        'authority': 'mms.pinduoduo.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'anti-content': '0aqAfa5e-wCElS_8XcJ5l7Gv83Bg8GipBieD5L5ejVMAHDxgU5NeLqQrViPNj_rquG8MfNVXRnvF-v9R575AeDuTQSKJx-z_Y03gAnaFSu9RC65deDhTQScJjBziVWr0GmE0LGX2uG7BQAxI96_vaV8HRo2YcmEOLnm2utMBDAah90_KaZ8H0_RbBmJqIZfe_1TQHkJUzdI-nL9mVeP6jvmqNP9_2i-7Xhx9YCWEFq0YhHtTZr6YCA2iPq7N9o6BsAqL97pty-zhAsMjXAJCcdi-sLlrCit78LGqo0xmurLWCesglQPn8JBnWrKgxjYXUKt4S1OiQvqmJhy45GqdUIqCdChlpi7h39SX3igQLrSfDvPQxAqcPpVboYitEuqoFAbQlTXqTYX5PjnGgynC_oqmYnuTqXGgan04oHqgyX0xJ9BVJ5Jtqq-ZezeFEzXsEjXhhFv-pUbZW1-ACEtBcs9zNGGZa7rTVTX0WTXI2z99-E-yCSveZkk4SJs2p-KJkFf8KUFR1DBbMIBeCSk8VJVh5J345-ejkUtL1MfjW-k4HJewW-b1W1BVHe32Z4SgfxEFFZd4uQZ-KPlFpXYnqWwXqeOYPCSmQztX9jSq0sP1mCaZt5XmJ3hmIvoumHhnhGPOgCxZgSxtp0PimqhPsIF26MmEem2mOY44AWXEti4ix98NaoGLkf9KxKN6qn0a8wDjb7cjaCLi6dYy_Jo990DaRpfYp32Z9N',
        'cache-control': 'max-age=0',
        'origin': 'https://mms.pinduoduo.com',
        'platform': '1',
        'referer': 'https://mms.pinduoduo.com/print/order/list',
        'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
        }

    cookies = read_file("config.yaml")["pdd_cookies"]
    res_dict = get_order(headers, cookies)
    order_list = res_dict['result']['orders']["list"]
    print("order_list====\n", type(order_list), "\n", order_list)
    for order in order_list:
        order_sn = order['orderSn']
        order_id = order['id']
        for good in order['detailList']:
            goods_id = good['id']
            goods_name = good['goodsName']
            goods_price = good['goodsPrice']
            url = query_link(goods_name, goods_price)
            print("订单号：\n{}\n商品名：\n{}\n某音链接：\n{}".format(order_sn, goods_name, url))
            # get_good_info(headers, cookies, good_id)
            # break


    # time.sleep(10)
    # de_list = decryption(headers, cookies)
    # de_list = de_1()
    # print("de_list====", de_list)


if __name__ == '__main__':
    main()
