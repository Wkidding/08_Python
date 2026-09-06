# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/7 06:53
@File   ：test_04
@IDE    ：PyCharm
=================================================="""

import pytest

# 使用用户自定义标记

def add(a,b):
    return a + b

class TestAdd:
    @pytest.mark.api
    def test_add_int(self):
        print("---test_add_int")
        res = add(1,3)
        assert res == 4

    @pytest.mark.web
    def test_add_str(self):
        print("---test_add_str")
        res = add("aaa","bbb")
        assert res == "aaabbb"

    @pytest.mark.ut
    def test_add_list(self):
        print("---test_add_list")
        res = add([1],[2,3,4])
        assert res == [1,2,3,4]

    @pytest.mark.login
    def test_add_float(self):
        print("---test_add_float")
        res = add(1.2,3.4)
        assert res == 4.6

    @pytest.mark.pay
    def test_add_number(self):
        print("---test_add_number")
        res = add(11,33)
        assert res == 44