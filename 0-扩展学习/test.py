# -*- coding: utf-8 -*-
# @Time    : 2021/09/02 16:44
# @Author  : hcy
# @Email   : Email@163.com
# @File    : test.py
# @Software: PyCharm

# with open("test.log", "r") as file:
#     # data = file.read()
#     # data2 = 'some data to be written to the file'
#     # file.write(data2)
#     data1 = file.readline()
#     data1 = data1.strip()
#     title = data1.split(",")
#     data2 = file.readlines()
#     all_datas = []
#     for i in data2:
#         i = i.strip().split(",")
#         va = []
#         for j in i:
#             va.append(j)
#         res = dict(zip(title, va))
#         all_datas.append(res)
#     print(all_datas)
    # title = file.readline()
    # for item in file:
    #     print(item)

with open("test.log", "r") as file:
    # data = file.read()
    # data2 = 'some data to be written to the file'
    # file.write(data2)
    data1 = file.readline()
    data1 = data1.strip()
    title = data1.split(",")
    data2 = file.readlines()

    tim = []
    for i in data2:
        i = i.strip().split(",")
        # print(i[2],type(i[2]))
        if i[2] == str(0):
            tim.append(int(i[1]))


    print(max(tim),min(tim),tim)
    avg = sum(tim)/len(tim)
    print("{:.2f}".format(avg))