# -*- coding: utf-8 -*-
# @Time    : 2021/09/02 14:06
# @Author  : hcy
# @Email   : Email@163.com
# @File    : load和loads区别.py
# @Software: PyCharm
import json
'''
json.load()是用来读取文件的，即，将文件打开然后就可以直接读取
json.loads()是用来读取字符串的

loads： 是将string转换为dict
dumps： 是将dict转换为string
load： 是将里json格式字符串转化为dict，读取文件
dump： 是将dict类型转换为json格式字符串，存入文件
'''

with open("文件名") as f:
     result=json.load(f)

with open("文件名") as file:
    line=file.readline()
    result=json.loads(line)