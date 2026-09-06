# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/15 07:28
@File   ：contest
@IDE    ：PyCharm
=================================================="""
"""
局部的conftest.py
"""

import pytest

@pytest.fixture()
def fun_login():
    print("--fun_login 登录(局部conftest.py)")
    yield
    print("--fun_login 登出(局部conftest.py)")

@pytest.fixture()
def fun_16_01(fun_login):
    print("---fun_16_01 ")


# @pytest.fixture(autouse=True, scope="function")
# def f0():
#     print("---fixture : function-前(局部f0)")
#     yield
#     print("---fixture : function-后(局部f0)")