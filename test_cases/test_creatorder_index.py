# -*- coding: utf-8 -*-
# @Time    : 2019/9/23/下午 7:12
# @Author  : XY
# @File    : test_creatorder_index.py

import unittest
from ddt import ddt,data
from common.my_log import MyLog
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from common import project_path
from common.read_config import ReadConfig
import json

#测试下单
test_data=DoExcel(project_path.case_path,'creatorder_index').read_data('CASE')#获取测试数据
my_log=MyLog()
token=None#定义token初始值为None
# aid = None#活动aid初始值为None


@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        self.t=DoExcel(project_path.case_path,'creatorder_index')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    # @unpack
    def test_cases(self,case):

        global token
        global aid
        global shopid
        global pid
        method = case['Method']
        path = case['Path']
        a = ReadConfig(project_path.conf_path).get_data('URL', 'agent_url')
        url = a + path
        params = eval(case['Params'])
        # 根据title定义请求参数
        if case['Title'] == '一元商品详情':
            params = {"shopId": shopid,"aid": aid}
        if case['Title'] == '一元商品下单' :
            params = {"orderType": "OneDollarRush","num": "1","pid": pid,"shopId": "1121","aid": "1163"}
            my_log.info('chuancanla{}'.format(params))
        if case['Title'] == '单笔数量超过20' :
            params = {"orderType": "OneDollarRush","num": "50","pid": pid,"shopId": "1121","aid": "1163"}

        headers = {'token': token}


        #发起测试
        my_log.info('-------正在测试【{}】模块里面第【{}】条测试用例：【{}】'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('-------接口URL:{}'.format(url))
        my_log.info('-------接口入参:{}'.format(params))
        my_log.info('-------请求方式:{}'.format(method))
        my_log.info('-------请求头headers:{}'.format(headers))
        my_log.info('-------预期结果:{}'.format(case["ExpectedResult"]))



        resp=HttpRequest().http_request(method,url,params,headers)#传参
        #根据用例title取变量
        if case['Title'] == '正常登录':
            try:
                token=resp.json()['token']
                my_log.info('-------------登录成功取到token')
            except Exception as e:
                my_log.info('-----------登录失败没取到token')
                raise e
        if case['Title'] == '首页查询':
            try:
                aid =resp.json()['shops'][0]['aid']
                shopid = resp.json()['shops'][0]['aid']
                my_log.info('-----------------已获取活动aid:{},shopid:{}'.format(aid,shopid))
            except Exception as e:
                my_log.error('-----------------未能取到活动aid')
        if case['Title'] == '一元商品详情':
            try:
                pid = resp.json()['doboShop']['periodList'][0]['pid']
                my_log.info('-----------------已获取最新周期pid:{}'.format(pid))
            except Exception as e:
                my_log.error('-----------------未取到最新周期pid')


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