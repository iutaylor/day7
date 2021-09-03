# -*- coding: utf-8 -*-
# @Time    : 2021/09/03 14:33
# @Author  : hcy
# @Email   : Email@163.com
# @File    : handle_extract_case.py
# @Software: PyCharm

import json
from Common.handle_data import EnvData
from jsonpath import jsonpath

from Common.handle_requests import send_requests


def extract_case(case, response):
    data = eval(case["extract_data"])

    for key,value in data.items():
        setattr(EnvData, key, str(jsonpath(response.json(), value)[0]))
        # print(getattr(EnvData,key))


if __name__ == '__main__':
    case = {"extract_data":'{"member_id":"$..id","token":"$..token"}'}
    login_url = "/member/login"
    login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
    resp = send_requests("POST",login_url,login_datas)
    extract_case(case,resp)
