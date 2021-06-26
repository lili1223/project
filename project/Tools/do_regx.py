# -*- coding: utf-8 -*-
# @Time : 2021/6/20 15:41
# @Author : 11858
# @Email : w1111@qq.com
# @File : do-regx.py
# @Project : Project
import re
# s='www.lemfix.com'#目标字符串
# res=re.match('(w)(ww)',s)  #全匹配 头部开始匹配
# print(res.group(2))   #group（）==group（0）拿到匹配的全字符 根据正则表达式里面的的括号去分组


# s='hellolemonfixlemon'
# res=re.findall('lemon',s)  #子字符串里面找匹配的内容
# #如有分组就是以元祖的形式表现出来 列表嵌套元祖
# print(res)

s='{"mobliephone":"${normal_tel}","passwoprd":123456}'
res=re.search("\${(.*?)}",s)
print(res)
print(res.group(0))
print(res.group(1))