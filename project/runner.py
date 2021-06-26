# -*- coding: utf-8 -*-
# @Time : 2021/5/23 16:42
# @Author : 11858
# @Email : w1111@qq.com
# @File : runner.py
# @Project : Project
from Tools.project_path import *
import HTMLTestRunner
from test_case.test_api import TestHttpRequest
import unittest
# from test_case import test_api_copy
from test_case import test_api
# TestHttpRequest.login()

'''
执行多个用例
'''
suite=unittest.TestSuite()
loder=unittest.TestLoader()
# suite.addTest(loder.loadTestsFromTestCase(TestHttpRequest))
suite.addTest(loder.loadTestsFromModule(test_api))
with open('report_path','wb')  as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2,title='测试一下',description="login_case",tester='lxl')
    runner.run(suite)
