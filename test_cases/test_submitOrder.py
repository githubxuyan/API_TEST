# -*- coding: utf-8 -*-
# @Time    : 2019/8/2/11:40
# @Author  : XY
# @File    : test_submitOrder.py


import unittest
from ddt import ddt,data
from common.my_log import MyLog
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from common import project_path
from common.get_data import GetData
from common.read_config import ReadConfig
import json

#测试下单
test_data=DoExcel(project_path.case_path,'submitOrder').read_data('submitOrderCASE')#获取测试数据
my_log=MyLog()
token=None#定义token初始值为None

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        self.t=DoExcel(project_path.case_path,'submitOrder')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    # @unpack
    def test_cases(self,case):

        global token
        method = case['Method']
        path = case['Path']
        a = ReadConfig(project_path.conf_path).get_data('URL', 'agent_url')
        url = a + path
        params = eval(case['Params'])
        headers = {'token': token}


        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('-------接口URL:{}'.format(url))
        my_log.info('-------接口入参:{}'.format(case["Params"]))
        my_log.info('-------请求头headers:{}'.format(headers))
        my_log.info('-------预期结果:{}'.format(case["ExpectedResult"]))



        resp=HttpRequest().http_request(method,url,params,headers)#传参
        #发请求后判断是否有token
        if case['Title'] == '正常登录':
            token=resp.json()['token']
            setattr(GetData,'token',resp.json()['token'])
            print(getattr(GetData,'token'))



        try:
            self.assertEqual(json.loads(case['ExpectedResult'])['msg'],resp.json()['msg'])
            self.assertEqual(json.loads(case['ExpectedResult'])['code'], resp.json()['code'])
            TestResult='Pass'#请注意这里
        except Exception as e:
        # except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
            raise e#抛出异常
        finally:
            self.t.write_back(case['CaseId']+1, 9, resp.text)#请注意这里
            self.t.write_back(case['CaseId']+1, 10, TestResult)

        my_log.info('-------实际结果：{}'.format(resp.json()))#http发送请求拿到的实际返回值