# -*- coding: utf-8 -*-
# @Time : 2021/5/23 17:40
# @Author : 11858
# @Email : w1111@qq.com
# @File : test.py
# @Project : Project

from Tools.http_request import HttpRequest
from test_case.do_excel import ReadExcel
from Tools.project_path import *
import unittest,json
from ddt import ddt,data
test_data=ReadExcel(case_data_path, 'login').get_data()
print(test_data)
@ddt  #使用ddt数据类型是列表嵌套列表 或者列表嵌套字典
class TestHttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_api(self,item):
        print(item)
if __name__ == '__main__':
    test_data=TestHttpRequest().test_api
    print(test_data)