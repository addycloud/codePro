import requests


def get_goods(search_str):
	cookies = {
		'Hm_lvt_87f2ef1ac0ed9d4bc756544ab4ada75e': '1684422024',
		'CMM_A_C_ID': 'b76e939d-f58c-11ed-be8b-167879f8c795',
		'_ga': 'GA1.1.1317481527.1684422024',
		'LOGIN-TOKEN-FORSNS-CX': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg3MDE0MDI5LCJpYXQiOjE2ODQ0MjIwMjksImlkIjo5MzA3MDIxNCwia2lkIjoiVVNFUi1DSVFPV05ZNUFXSFMtQUtBQ0YyIn0._Y7KDxEaAQ90yBPMXu0XfwEUdGWXyNTGvPWj4q18hr4',
		'_ga_BBZXS8H6XZ': 'GS1.1.1684422024.1.1.1684422074.0.0.0',
		'Hm_lpvt_87f2ef1ac0ed9d4bc756544ab4ada75e': '1684422075',
	}

	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
		'Connection': 'keep-alive',
		'Origin': 'https://www.chanxuan.com',
		'Referer': 'https://www.chanxuan.com/',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
		'X-Authorization-Cx': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg3MDE0MDI5LCJpYXQiOjE2ODQ0MjIwMjksImlkIjo5MzA3MDIxNCwia2lkIjoiVVNFUi1DSVFPV05ZNUFXSFMtQUtBQ0YyIn0._Y7KDxEaAQ90yBPMXu0XfwEUdGWXyNTGvPWj4q18hr4',
		'X-Client-Id': '3345333948',
		'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'x-platform-id': '10009',
	}

	params = {
		'request_id': '3c8b75e4c7739a1de8fc5be6eddc10ac',
		'sort_column': 'base_score',
		'day_type': '2',
		'order_by': 'desc',
		'search_str': search_str,  # '【超值100片装】眼镜擦拭湿巾纸 除尘去油速干无痕擦拭镜片布屏幕',
		'cos_ratio': '',
		'free_sample_condition': '0',
		'service_guarantee': '0',
		'shop_score': '',
		'volume': '',
		'shareable': '1',
		'pv_count': '',
		'author_count': '',
		'activity_price': '',
		'has_video': '1',
		'has_live': '1',
		'banner_id': '',
		'is_free_sample': '0',
		'cmm_cid': '0',
		'cmm_cid_snd': '0',
		'cmm_cid_third': '0',
		'cmm_cid_fourth': '0',
		'cmm_cid_fifth': '0',
		'most_aweme_volume': '0',
		'most_live_volume': '0',
		'has_douyin_goods_tag': '0',
		'is_assured': '0',
		'has_shop_brand_tag': '0',
		'page': '1',
		'size': '10',
		'total_page': '0',
	}

	response = requests.get('https://api-service.chanxuan.com/v1/home/getGoodsPage', params=params, cookies=cookies,
	                        headers=headers)
	return response.json()


def get_the_goods(goods, _price):
	max_good = None
	max_activity_cos_fee = 0

	for good in goods['data']['list']:
		if good['price'] == _price and good['activity_cos_fee'] > max_activity_cos_fee:
			max_good = good
			max_activity_cos_fee = good['activity_cos_fee']

	if max_good:
		return max_good['detail_url']
	else:
		print('The good with price of 1280 and maximum activity_cos_fee is not found.')
		return None


def get_link(detail_url):
	import requests

	cookies = {
		'Hm_lvt_87f2ef1ac0ed9d4bc756544ab4ada75e': '1684422024',
		'CMM_A_C_ID': 'b76e939d-f58c-11ed-be8b-167879f8c795',
		'_ga': 'GA1.1.1317481527.1684422024',
		'LOGIN-TOKEN-FORSNS-CX': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg3MDE0MDI5LCJpYXQiOjE2ODQ0MjIwMjksImlkIjo5MzA3MDIxNCwia2lkIjoiVVNFUi1DSVFPV05ZNUFXSFMtQUtBQ0YyIn0._Y7KDxEaAQ90yBPMXu0XfwEUdGWXyNTGvPWj4q18hr4',
		'Hm_lpvt_87f2ef1ac0ed9d4bc756544ab4ada75e': '1684423249',
		'_ga_BBZXS8H6XZ': 'GS1.1.1684422024.1.1.1684423517.0.0.0',
	}

	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
		'Connection': 'keep-alive',
		'Origin': 'https://www.chanxuan.com',
		'Referer': 'https://www.chanxuan.com/',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
		'X-Authorization-Cx': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBpZCI6IjEwMDA5IiwiZXhwIjoxNjg3MDE0MDI5LCJpYXQiOjE2ODQ0MjIwMjksImlkIjo5MzA3MDIxNCwia2lkIjoiVVNFUi1DSVFPV05ZNUFXSFMtQUtBQ0YyIn0._Y7KDxEaAQ90yBPMXu0XfwEUdGWXyNTGvPWj4q18hr4',
		'X-Client-Id': '3345333948',
		'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'x-platform-id': '10009',
	}

	json_data = {
		'product_url': detail_url,'type': 0,
		'need_external_info': False,
		'source': 'jx_dk_pc_copy',
	}

	response = requests.post('https://api-service.chanxuan.com/v1/douke/sharelink/product', cookies=cookies, headers=headers, json=json_data)
	return response.json()


def query_link(title, price):
	goods = get_goods(title)
	the_url = get_the_goods(goods, price)
	return get_link(the_url)["data"]["dk_password"]


def main():
	title = "【超值100片装】眼镜擦拭湿巾纸 除尘去油速干无痕擦拭镜片布屏幕"
	price = 1280
	url = query_link(title, price)
	print(url)


if __name__ == '__main__':
	main()
