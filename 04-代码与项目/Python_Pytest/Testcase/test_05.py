# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/7 07:47
@File   ：test_05
@IDE    ：PyCharm
=================================================="""

import pytest

# 使用pytest框架内置标记

def add(a,b):
    return a + b

class TestAdd:
    @pytest.mark.skip
    def test_add_int(self):
        print("---test_add_int")
        res = add(1,3)
        assert res == 4

    # 使用满足条件跳过，其中条件为1=2，显然是不满足的，因此该用例仍会执行
    @pytest.mark.skipif("1==2")
    def test_add_str(self):
        print("---test_add_str")
        res = add("aaa","bbb")
        assert res == "aaabbb"

    # 断言相等，用例通过
    @pytest.mark.xfail
    def test_add_list_01(self):
        print("---test_add_list_01")
        res = add([1],[2,3,4])
        assert res == [1,2,3,4]

    # 断言不相等，用例失败
    @pytest.mark.xfail
    def test_add_list_02(self):
        print("---test_add_list_02")
        res = add([1],[2,3,4])
        assert res != [1,2,3,4]