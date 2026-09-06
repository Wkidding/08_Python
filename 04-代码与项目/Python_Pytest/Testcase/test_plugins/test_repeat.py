# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/23 07:02
@File   ：test_repeat
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 重新测试pytest-repeat
"""

import pytest

class Test_01:
    def test_01(self):
        print('测试用例第一条')
    def test_02(self):
        print('测试用例第二条')
    def test_03(self):
        print('测试用例第三条')


@pytest.mark.repeat(3)
def test_repeat_decorator ( ):
    print("测试用例执行")

class TestCase02:
    @pytest.mark.repeat(3)
    def test_02 (self):
        print("---用例2执行---")


class TestCase03:
    @pytest.mark.repeat(2)
    def test_01 (self):
        print('测试用例第一条')

    @pytest.mark.repeat(3)
    def test_02 (self):
        print('测试用例第二条')

    @pytest.mark.repeat(4)
    def test_03 (self):
        print('测试用例第三条')




import random
import time

class TestCase04:
    def test_func(self):
        computer = random.randint(0, 4)
        time.sleep(1)
        print(computer)
        assert computer < 3

