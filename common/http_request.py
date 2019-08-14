# -*- coding: utf-8 -*-
# @Time    : 2019/7/9/16:49
# @Author  : XY
# @File    : http_request.py

import requests

class HttpRequest:
    '''该类完成http的get 以及post请求，并返回结果'''

    def http_request(self,method,url,param,headers):#对象方法
        '''根据请求方法来决定发起get请求还是post请求
        method: get post http的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文
        '''

        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,headers=headers)#
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,headers=headers)#传递cookies
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp=None
        return resp

#测试代码
if __name__ == '__main__':
    from common .read_config import ReadConfig
    from common import project_path
    from common.do_excel import DoExcel
    import json

    test_data = DoExcel(project_path.case_path, 'main').read_data('LoginCASE')  # 获取测试数据
    a = ReadConfig(project_path.conf_path).get_data('URL', 'sys_url')
    url = a + test_data[10]['Path']
    params = test_data[10]['Params']
    params=eval(params)
    method = test_data[10]['Method']
    # print(method, url, params)

    # print(params)
    res = HttpRequest().http_request(method,url,params,headers={'token':'60b5aa2cce1ba22803d5689286cb728e','Content-Type': 'application/json'})
    print(res.json()['pageList']['data'][0]['id'])
    # print(res.json())




