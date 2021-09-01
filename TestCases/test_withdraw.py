# -*- coding: utf-8 -*-
# @Time    : 2021/09/01 11:30
# @Author  : hcy
# @Email   : Email@163.com
# @File    : test_withdraw.py
# @Software: PyCharm
import json
import unittest
from jsonpath import jsonpath
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_phone import get_old_phone
from Common.handle_requests import send_requests
from Common.myddt import ddt,data
from Common.handle_data import replace_mark_with_data
from Common.handle_db import HandleDB
from Common.my_logger import logger

he = HandleExcel(datas_dir+"\\api_cases.xlsx", "提现")
cases = he.read_all_datas()
he.close_file()
db = HandleDB()


@ddt
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  提现模块用例 执行开始  ========")
        user,passwd = get_old_phone()
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": passwd})
        cls.member_id = jsonpath(resp.json(), "$..id")[0]
        cls.token = jsonpath(resp.json(), "$..token")[0]

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  提现模块用例 执行结束  ========")


    @data(*cases)
    def test_recharge(self, case):
        logger.info("*********   执行用例{}：{}   *********".format(case["case_id"], case["title"]))
        # 替换的数据
        if case["request_data"].find("#member_id#") != -1:
            case = replace_mark_with_data(case, "#member_id#", str(self.member_id))

        # 数据库 - 查询当前用户的余额 - 在充值之前
        if case["check_sql"]:
            bef_money = db.select_one_data(case["check_sql"])["leave_amount"]
            logger.info("提现前的用户余额：{}".format(bef_money))
            # 期望的用户余额。 充值之前的余额 + 充值的钱
            recharge_money = json.loads(case["request_data"])["amount"]
            logger.info("提现的金额为：{}".format(recharge_money))
            exp_money = round(float(bef_money) - float(recharge_money),2)
            logger.info("期望的提现后的金额为：{}".format(exp_money))
            # 更新期望的结果 - 将期望的用户余额更新到期望结果当中。
            case = replace_mark_with_data(case, "#money#", str(exp_money))
        # 将期望的结果转成字典对象，再去比对
        # logger.info("表格数据{}{}".format(case["expected"],type(case)))
        expected = json.loads(case["expected"])
        logger.info("用例的期望结果为：{}".format(expected))
        # 发起请求 - 给用户充值
        response = send_requests(case["method"],case["url"], eval(case["request_data"]),token=self.token)

        # 断言
        try:
            self.assertEqual(response.json()["code"],expected["code"])
            self.assertEqual(response.json()["msg"],expected["msg"])
            # 数据库 - 查询当前用户的余额
            if case["check_sql"]:
                self.assertEqual(response.json()["data"]["id"], expected["data"]["id"])
                self.assertEqual(response.json()["data"]["leave_amount"], expected["data"]["leave_amount"])
                real_money = db.select_one_data(case["check_sql"])["leave_amount"]
                logger.info("充值后的用户余额：{}".format(real_money))
                self.assertEqual("{:2f}".format(expected["data"]["leave_amount"]),"{:2f}".format(float(real_money)))
        except:
            logger.exception("断言失败！")
            raise

