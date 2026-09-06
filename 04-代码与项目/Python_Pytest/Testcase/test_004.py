# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/6 07:00
@File   ：test_04
@IDE    ：PyCharm
=================================================="""
## 默认用例执行顺序

import pytest

def setup_module ():
    print("初始化：setup_module")

def teardown_module ():
    print("清理：teardown_module")

def setup_function ():
    print("初始化：setup_function")

def teardown_function ():
    print("清理：teardown_function")


def test_f ( ):
    print("--------------test_f")


class Test01:
    def setup_class (self):
        print("初始化：setup_class1")

    def teardown_class (self):
        print("清理：teardown_class1")

    def setup_method (self):
        print("初始化：setup_method1")

    def teardown_method (self):
        print("清理：teardown_method1")

    def test_d (self):
        print("--------------test_d")

    def test_c (self):
        print("--------------test_c")


class Test02:
    def setup_class (self):
        print("初始化：setup_class2")

    def teardown_class (self):
        print("清理：teardown_class2")

    def setup_method (self):
        print("初始化：setup_method2")

    def teardown_method (self):
        print("清理：teardown_method2")

    def test_b (self):
        print("--------------test_b")

    def test_a (self):
        print("--------------test_a")


def test_e ():
    print("--------------test_e")
