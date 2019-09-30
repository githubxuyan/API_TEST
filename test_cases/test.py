# -*- coding: utf-8 -*-
# @Time    : 2019/9/24/上午 11:01
# @Author  : XY
# @File    : test.py

import requests

url = 'http://wapapi.overseas.lihvip.com/index/shop.do'
headers = {'token': 'QsNUB6sqsEfBRWVuuQy0DpPrv6P8nMiS_GoDoRnpDKg3Jt2Ai56sbxxNboLxv29e0-GUwqj8DYH7111AjDowTw'}
resp = requests.get(url,headers=headers)
# print(resp.json())
print(resp.json()['shops'][0]['shopId'])