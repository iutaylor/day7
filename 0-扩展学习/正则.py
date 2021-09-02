# -*- coding: utf-8 -*-
# @Time    : 2021/09/02 09:50
# @Author  : hcy
# @Email   : Email@163.com
# @File    : 正则.py
# @Software: PyCharm
import re
from Common.handle_config import conf
from Common.handle_data import EnvData

data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'
setattr(EnvData,"user_money",250)

res = re.findall("#(.*?)#",data) # 如果没有找到，返回的是空列表。
print(res)

# 标识符对应的值，来自于：1、环境变量  2、配置文件
if res:
    for item in res:
        # 得到标识符对应的值。
        try:
            value = conf.get("data",item)
        except:
            value = getattr(EnvData,item)
        print(value)
        # 再去替换原字符串
        data = data.replace("#{}#".format(item),str(value))
    print(data)

'''
从ini来的数据为字符串格式
从excel获取每个表格值为字符串格式
从json获取的值为本来格式
'''