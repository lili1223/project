# -*- coding: utf-8 -*-
# @Time : 2021/6/3 18:37
# @Author : 11858
# @Email : w1111@qq.com
# @File : do_mysql.py
# @Project : Project

import mysql.connector
#创建数据库连接
cnn=mysql.connector.connect()
config={
    'host':'',
    'user':'',
}
#创建一个数据库连接
cnn=mysql.connector.connect(**config)

#游标cursor
cursor=cnn.cursor()

#sql语句存储在字符串里面

















