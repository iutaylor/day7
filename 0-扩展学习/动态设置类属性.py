"""
======================
Author: 柠檬班-小简
Time: 2020/7/8 21:38
Project: day7
Company: 湖南零檬信息技术有限公司
======================
"""

class AABB:

    cc = "hello"
    pass

# setattr,hasattr,getattr,delattr

setattr(AABB,"namw","123")
print(AABB.namw)
print(hasattr(AABB,"namw"))
print(getattr(AABB,"namw"))
delattr(AABB,"namw")
print(getattr(AABB,"cc"))