# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 20:52
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py


import unittest
from ext import HTMLTestRunnerNew
from common import project_path
from test_cases import test_login#具体到模块
from test_cases import test_main_process


#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_submitOrder))
suite.addTest(loader.loadTestsFromModule(test_main_process))

#执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='商城主流程接口',
                                            description='主流程业务',
                                            tester='技术----许彦')
    runner.run(suite)#执行用例  传入suite suite里面是我们收集的测试用例
