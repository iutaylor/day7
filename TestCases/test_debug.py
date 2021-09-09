# -*- coding: utf-8 -*-
# @Time    : 2021/09/07 14:40
# @Author  : hcy
# @Email   : Email@163.com
# @File    : test_debug.py
# @Software: PyCharm
import unittest

from Common.handle_db import HandleDB

data1 = {
        "member_id":123626069,
        "title":"123",
        "amount":1000,
        "loan_rate":10,
        "loan_term":1,
        "loan_date_type":1,
        "bidding_days":5
        }
class TestDebug(unittest.TestCase):

    def test_debug(self):
        db = HandleDB()
        data2 = db.select_one_data("SELECT * FROM  futureloan.loan WHERE member_id=123626069;")
        print(data2)
        # print(data["title"], data["amount"], data["loan_rate"], data["loan_rate"], data["loan_date_type"],
        #       ["bidding_days"])
        self.assertEqual(data1["title"],data2["title"])
        self.assertEqual(data1["amount"], data2["amount"])
        self.assertEqual(data1["loan_rate"], data2["loan_rate"])
        self.assertEqual(data1["loan_term"], data2["loan_term"])
        self.assertEqual(data1["loan_date_type"], data2["loan_date_type"])
        self.assertEqual(data1["bidding_days"], data2["bidding_days"])