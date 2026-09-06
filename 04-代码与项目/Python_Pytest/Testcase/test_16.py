# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/15 07:21
@File   ：test_16
@IDE    ：PyCharm
=================================================="""
"""
fixture跨模块共享conftest.py
"""
import pytest

## 1、使用局部的conftest.py
# def test_16_a(fun_login):
#     print("--------------test_16_a")





## 2、使用全局的conftest.py
# def test_16_b(fun_login):
#     print("--------------test_16_b")






## 3、当全局和局部conftest.py都有同名fixture时
def test_16_c(fun_login):
    print("--------------test_16_c")
