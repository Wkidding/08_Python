# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/14 06:37
@File   ：test_14
@IDE    ：PyCharm
=================================================="""
"""
fixture实现自定义前置、后置
"""

import pytest


@pytest.fixture()
def fun_01():
    print("---前置：登录")
    yield
    print("---后置：退出")

def test_01_a(fun_01):
    print("--------------test_01_a")

class Test01:
    def test_01_b (self, fun_01):
        print("--------------test_01_b")

    def test_01_c (self):
        print("--------------test_01_c")





@pytest.fixture()
def fun_02 (request):
    print("---前置：登录")

    def after():
        print("---后置：退出")

    request.addfinalizer(after)

def test_02_a (fun_02):
    print("--------------test_a")

class Test02:
    def test_02_b (self, fun_02):
        print("--------------test_b")

    def test_02_c (self):
        print("--------------test_c")





@pytest.fixture()
def fun_03():
    print("---前置")
    raise Exception("自定义异常")
    yield
    print("---后置")

def test_03_a (fun_03):
    print("--------------test_a")





@pytest.fixture()
def fun_04():
    print("---前置")
    yield
    print("---后置")

def test_04_a(fun_04):
    print("--------------test_04_a")
    raise Exception("自定义异常")