# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 20:52
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py


import unittest
from ext import HTMLTestRunnerNew
from common import project_path
from test_cases import test_login#具体到模块
from test_cases import test_phone
from test_cases import test_list
from test_cases import  test_creatorder_index


#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_phone))
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_list))
suite.addTest(loader.loadTestsFromModule(test_creatorder_index))

#执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='接口自动化',
                                            description='一元夺宝app接口',
                                            tester='测试----许彦')
    runner.run(suite)#执行用例  传入suite suite里面是我们收集的测试用例
