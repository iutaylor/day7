# -*- coding: utf-8 -*-
# @Time    : 2021/09/02 11:50
# @Author  : hcy
# @Email   : Email@163.com
# @File    : test_login.py
# @Software: PyCharm

''''
登录接口
获取数据》请求》断言，不做数据库校验
'''
import unittest
import json
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.myddt import ddt,data
from Common.my_logger import logger
from Common.handle_requests import send_requests

excel = HandleExcel(datas_dir + "\\api_cases.xlsx","登录")
cases = excel.read_all_datas()
excel.close_file()


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("----------登录模块用例执行开始----------")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("----------登录模块用例执行结束----------")

    @data(*cases)
    def test_login(self, case):
        logger.info("*****执行用例{}：{}".format(case["case_id"],case["title"]))
        #发请求
        response = send_requests(case["method"], case["url"], case["request_data"])
        # 记录期望数据
        expected = json.loads(case["expected"])
        logger.info("期望的响应结果{}".format(expected))
        # 断言
        self.assertEqual(response.json()["code"],expected["code"])
        self.assertEqual(response.json()["msg"], expected["msg"])


