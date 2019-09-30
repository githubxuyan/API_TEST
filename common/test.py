# dict={'a':1,'b':2,'c':3}
# test_data=[]
# for i in dict.keys():
#     new_dict=dict.copy()
#     new_dict[i]=''
#     test_data.append(new_dict)
# print(test_data)
import requests

res=requests.get('http://wapapi.overseas.lihvip.com/index/shop.do',params=None)
print(res.json())