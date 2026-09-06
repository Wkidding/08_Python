# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/25 14:15
@File   ：test_order
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 控制函数执行顺序pytest-ordering
"""

import pytest

## 使用 `@pytest.mark.order(n)` 装饰器，**数字越小越先执行**
# @pytest.mark.order(2)
# def test_login():
#     print("执行登录")
#
# @pytest.mark.order(1)
# def test_register():
#     print("执行注册")
#
# @pytest.mark.order(3)
# def test_create_order():
#     print("创建订单")
#
#


# @pytest.mark.order(-1)      # 最后一个执行
# def test_logout():
#     print("登出")
#
# @pytest.mark.order(1)       # 第一个执行
# def test_login():
#     print("登录")
#
# @pytest.mark.order(-2)      # 倒数第二个执行
# def test_cleanup():
#     print("清理数据")
#
#
# @pytest.mark.order("last")
# def test_create_order():
#     print("创建订单")
#
# @pytest.mark.order("second")
# def test_login():
#     print("登录")
#
# @pytest.mark.order("first")
# def test_register():
#     print("注册")


# @pytest.mark.order(1)
# def test_register():
#     print("注册")
#
# @pytest.mark.order(after="test_register")
# def test_login():
#     print("登录（在注册之后执行）")
#
# @pytest.mark.order(before="test_logout")
# def test_create_order():
#     print("创建订单（在登出之前执行）")
#
# @pytest.mark.order(2)
# def test_logout():
#     print("登出")



@pytest.mark.order(1)
def test_a():
    print("测试A")

@pytest.mark.order(2)
def test_b():
    print("测试B")

@pytest.mark.order(after="test_b")
def test_c():
    print("测试C（在B之后执行）")

# 未指定顺序的用例默认排在最后
def test_d():
    print("测试D（默认最后执行）")