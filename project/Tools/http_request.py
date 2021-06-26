# -*- coding: utf-8 -*-
# @Time : 2021/5/23 15:52
# @Author : 11858
# @Email : w1111@qq.com
# @File : http_request.py
# @Project : Project
'''
1、可配置代理proxies={"http":"http://127.0.0.1:8888","https":"https://127.0.0.1:8888"}
2、verify=False
'''
import requests
import json
# class HttpRequest:
#     @staticmethod
#     def http_request(url,data,method,headers=None):
#         try:
#             if method.lower() == 'get':
#                 res = requests.get(url, data,headers=None)
#             elif method.lower() == 'post':
#                 res = requests.post(url, data,headers=None)
#             else:
#                 print('输入错误')
#             return res
#         except Exception as e:
#             print('出错了，错误是：{}'.format(e))
#             raise e
# if __name__ == '__main__':
#     url = 'https://wry-test-jh.iauto360.cn/pc/user/bizuser/pwd-login'
#     data = {"password": "84ea34b048b95c3a985f95278b8b75ed", "account": "820573"}
#     res=HttpRequest.http_request(url,json.dumps(data),'post')
#     print(res.json())

import datetime
import calendar
import requests
import  json
import time
class HttpRequest:
    @classmethod
    def http_request(self,url,data,method,headers=None,token=None,verify=False,
             proxies=None):
        '''利用requests封装get 请求和post请求
            url：请求的地址 http://xxx：port
            param：传递函数 非必填参数字典的格式传递参数
            cookie：请求的时候传递的cookies值
            method：请求方法 支持时候传递的get 以及post 字符串形式的参数
        '''
        if method.lower()=='get':
            res=requests.get(url,data)
            return res
        else:
            proxies={"http":"http://127.0.0.1:8888","https":"https://127.0.0.1:8888"}
            res = requests.post(url,data,verify=False,headers=headers,proxies=proxies)
            return res
if __name__ == '__main__':
    header = {'user-agent': "Mozilla/5.0", 'content-type': "application/json;charset=UTF-8", 'token': None}
    url='https://wry-test-jh.iauto360.cn/pc/user/bizuser/pwd-login'
    data={"password":"84ea34b048b95c3a985f95278b8b75ed","account":"820573"}
    res=HttpRequest().http_request(url,json.dumps(data),'post',headers=header)
    print(res.json())
    print(res.request.headers)