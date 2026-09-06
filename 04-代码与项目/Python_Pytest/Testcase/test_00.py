# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/5 21:51
@File   ：test
@IDE    ：PyCharm
=================================================="""
import pytest

def inc (x):
    return x + 1

def test_a ( ):
    print("---test_a")
    assert inc(0) == 1


class TestDemo1:
    def test_b (self):
        print("---test_b")
        assert "D" in "Demo"

    def test_c (self):
        print("---test_c")
        assert "em" in "Demo"


class TestDemo2:
    def test_d (self):
        print("---test_d")
        assert "mo" in "Demo"


def add(a,b):
    return a + b

class TestAdd:
    def test_add_int(self):
        print("---test_add_int")
        res = add(1,3)
        assert res == 4

    def test_add_str(self):
        print("---test_add_str")
        res = add("aaa","bbb")
        assert res == "aaabbb"

    def test_add_list(self):
        print("---test_add_list")
        res = add([1],[2,3,4])
        assert res == [1,2,3,4]