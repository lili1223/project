# -*- coding: utf-8 -*-
# @Time : 2021/5/23 16:29
# @Author : 11858
# @Email : w1111@qq.com
# @File : test_api.py
# @Project : Project
from Tools.http_request import HttpRequest
from test_case.do_excel_copy import ReadExcel
from Tools.project_path import *
import unittest,json
from ddt import ddt,data
'''
1、#使用ddt数据类型是列表嵌套列表 或者列表嵌套字典
2、配置文件读取出来的数据格式都是字符串，需要eval()一下，变成原本的数据格式
'''
test_data=ReadExcel(case_data_path).get_data()
# print(test_data)
Token=None
@ddt
class TestHttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_api(self,item):
        global Token
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*',
            'Connection': 'keep-alive', 'Content-Length': '78',
             "token": Token}
        res = HttpRequest().http_request(item['url'], eval(json.dumps(item['data'])), item['method'],headers=headers)
        print('请求头：',res.request.headers)
        print(item)
        if Token==None:
            Token=res.json()['data']['token']
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            result='PASS'  #用例执行失败就不会在执行
        except Exception as e:
            print('出错啦，错误是：{}'.format(e))
            result='failed'
            raise e
        finally:
            ReadExcel(case_data_path).wrire_back(item['sheet_name'],item['case_id'] + 1, str(res.json()),result)
            print('请求返回的结果是：{}'.format(res.json()))
            #写之前需要先把表格关闭在写入，写入表格的数据只能写入字符串了日行的
    # @staticmethod
    # def login():  # 接口用例
    #     global Token
    #     res = HttpRequest().http_request("https://wry-test-jh.iauto360.cn/pc/user/bizuser/pwd-login",
    #                              json.dumps({"password": "84ea34b048b95c3a985f95278b8b75ed", "account": "820573"}),
    #                              "post")
    #     Token = res.json()['data']['token']
    #     try:
    #        assert res.status_code == 200
    #     except AssertionError as e:
    #         print('test_api‘s error is :{}'.format(e))
    #         raise e
    #     finally:
    #         print('请求结果：', res.json())


if __name__ == '__main__':
    TestHttpRequest.test_api()

