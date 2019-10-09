# -*- coding: utf-8 -*-
# @Time    : 2019/9/24/上午 11:01
# @Author  : XY
# @File    : test.py

import requests

url = 'http://wapapi.test.lihuitreasure.com/shop/getDoboShopDetail.do'
headers = {'token': 'N5SsK04JWK8JImrTnLFvX-uoS6MNFcSlli_p9tGrvpYpvJYEOZ8uGSki-NYeHvVFOlaVn1LJgstm6GBO4xNOlQ'}
params = {
    "shopId": "175",
    "aid": "175"
}
resp = requests.get(url,params,headers=headers)
# print(resp.json())
print(resp.json()['doboShop']['periodList'][0]['pid'])