# -*- coding: utf-8 -*-
# @Time : 2021/5/23 15:59
# @Author : 11858
# @Email : w1111@qq.com
# @File : project_path.py
# @Project : Project
#配置文件路径
import os
#获取当前项目的顶级文件目录
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
#获取测试数据的路径
case_data_path=os.path.join(project_path,'test_data','case_data.xlsx')
# print(case_data_path)
#获取测试报告位置
report_path=os.path.join(project_path,'test_report','report.html')
print(report_path)
#获取配置文件路径
config_path=os.path.join(project_path,'conf','case.config')
# print(config_path)
