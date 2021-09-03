# -*- coding: utf-8 -*-
# @Time    : 2021/09/03 10:20
# @Author  : hcy
# @Email   : Email@163.com
# @File    : test_user_business.py
# @Software: PyCharm
import json
from jsonpath import jsonpath
import unittest
from Common.handle_data import replace_mark_by_regular,clear_EnvData_attrs,EnvData
from Common.myddt import ddt,data
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_requests import send_requests
from Common.handle_extract_case import extract_case

excel = HandleExcel(datas_dir + "\\api_cases.xlsx", "业务流")
cases = excel.read_all_datas()


@ddt
class TestBusiness(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        clear_EnvData_attrs()

    @data(*cases)
    def test_business(self, case):
        case = replace_mark_by_regular("#(.*?)#", case)
        if hasattr(EnvData, "token"):
            resp = send_requests(case["method"], case["url"], case["request_data"],token=EnvData.token)
        else:
            resp = send_requests(case["method"], case["url"], case["request_data"])

        if case["extract_data"]:
            extract_case(case,resp)
