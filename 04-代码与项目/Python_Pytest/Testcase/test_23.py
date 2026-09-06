# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/20 07:37
@File   ：test_23
@IDE    ：PyCharm
=================================================="""
"""
 indirect参数设置的区别
"""

import pytest


"""
indirect 默认为 False
"""
data = ["aaa", "ren", "jack"]
@pytest.mark.parametrize("register", data)
def test_case_01 (register):
    print(f"register={register}")

"""
indirect设置为False，和不指定时结果一致
"""
@pytest.mark.parametrize("register", data, indirect=False)
def test_case_02 (register):
    print(f"register={register}")






# 1. 定义一个 fixture
@pytest.fixture
def db_query(request):
    # request.param 接收从 parametrize 传来的值
    query_param = request.param
    if query_param == "user1":
        return {"id": 1, "name": "Alice"}
    elif query_param == "user2":
        return {"id": 2, "name": "Bob"}

# 2. 在 parametrize 中引用这个 fixture，并设置 indirect=True
@pytest.mark.parametrize("db_query", ["user1", "user2"], indirect=True)
def test_user_query(db_query):
    # db_query 现在已经是 fixture 返回的字典了，而不是字符串 "user1" 或 "user2"
    print(db_query)  # 输出: {'id': 1, 'name': 'Alice'} 等
    assert "name" in db_query
