"""
======================
Author: 柠檬班-小简
Time: 2020/7/6 20:19
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
import re
from Common.handle_config import conf
import json

"""
1、一条用例涉及到数据当中，有url、request_data、check_sql

"""


class EnvData:
    """
    存储用例要使用到的数据。
    """
    pass
def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)



def replace_mark_by_regular(mark,data):
    ''''
    整条数据替换：
    思路1：遍历每行的每个值，进行替换替换
    思路2：case转换成json字符串，替换后，再转成json字典（下面方法使用）,data要为字典
    '''
    data = json.dumps(data, ensure_ascii=False)
    res = re.findall(mark, data)  # 如果没有找到，返回的是空列表。
    # 标识符对应的值，来自于：1、环境变量  2、配置文件
    if res:
        for item in res:
            # 得到标识符对应的值。
            try:
                value = conf.get("data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    continue
            # print(value)
            # 再去替换原字符串
            data = data.replace("#{}#".format(item), str(value))
        return json.loads(data)


def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    # case = {
    #     "method": "POST",
    #     "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
    #     "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    # }
    # if case["request_data"].find("#phone#") != -1:
    #     case = replace_mark_with_data(case, "#phone#", "123456789001")
    # for key,value in case.items():
    #     print(key,value)

    # data = {"member_id":"#member_id#","amount":600, "money":"#user_money#","username": "#user#", "passwd": "#passwd#"}
    # # data = {"code":0,"msg":"OK","data":{"id":"#member_id#","leave_amount":"#money#"}}
    # # data_str = json.dumps(data, ensure_ascii=False)
    # data1 = "123456"
    setattr(EnvData, "user_money", 250)
    # # data = replace_mark_by_regular("#(.*?)#",data)
    # data = replace_mark_by_regular("#(user_money)#",data)
    #
    # print(data,type(data))
    clear_EnvData_attrs()
    print("123")