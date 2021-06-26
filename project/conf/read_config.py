# -*- coding: utf-8 -*-
# @Time : 2021/5/23 16:08
# @Author : 11858
# @Email : w1111@qq.com
# @File : read_config.py
# @Project : Project
import configparser
from Tools.project_path import *
class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(config_path)
        res=cf[section][option]
        return res
if __name__ == '__main__':
    res=ReadConfig.get_config(config_path,'MODE','mode')
    print(res)