# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/9 06:32
@File   ：test_07
@IDE    ：PyCharm
=================================================="""

import pytest
import platform
import sys

@pytest.mark.skip
def test_case_01():
    print("代码开发中")

@pytest.mark.skip(reason="代码开发中")
def test_case_02():
    print("---skip")


def test_case_03():
    if platform.system() == "Windows":
        pytest.skip("win下跳过")
        print("---skip")
    else:
        print("不跳过")

@pytest.mark.skip(reason="代码开发中")
class TestCase04:
    def test_case_04_1(self):
        print("test_case1---skip")
    def test_case_04_2(self):
        print("test_case2---skip")

# 在条件满足时跳过整个模块
# if sys.platform == "win32":
#     pytest.skip('win中该模块跳过', allow_module_level=True)
class TestCase05:
    def test_case_05_1 (self):
        print("test_case1---skip")

    def test_case_05_2 (self):
        print("test_case2---skip")

def test_case_05_3 ( ):
    print("test_case3---skip")

def test_case_05_4 ( ):
    print("test_case4---skip")


# pytestmark = pytest.mark.skip(reason="win中该模块跳过")
class TestCase06:
    def test_case_06_1(self):
        print("test_case1---skip")
    def test_case_06_2(self):
        print("test_case2---skip")

def test_case_06_3():
    print("test_case3---skip")
def test_case_06_4():
    print("test_case4---skip")


@pytest.mark.skipif
def test_case_07():
    print("---skipif")
    assert 1==1

@pytest.mark.skipif(sys.platform.startswith("win"), reason="win环境中跳过")
def test_case_08_1():
    pass

@pytest.mark.skipif(sys.version_info < (3, 9), reason="python3.9以下跳过")
def test_case_08_2():
    pass


@pytest.mark.skipif(sys.platform.startswith("win"), reason="win环境中跳过")
class TestCase09:
    def test_case_09_1 (self):
        print("test_case1---skip")

    def test_case_09_2 (self):
        print("test_case2---skip")

def test_case_09_3 ( ):
    print("test_case3---skip")

def test_case_09_4 ( ):
    print("test_case4---skip")


pytestmark = pytest.mark.skipif(sys.platform=="win32", reason="win中该模块跳过")
def test_case_10_1():
    print("test_case1---skip")
def test_case_10_2():
    print("test_case2---skip")


# @pytest.importorskip("requestsx", minversion="2.31.0")
# def test_case11():
#     print("---importorskip")


@pytest.importorskip("requests", minversion="3.31.0")
def test_case12():
    print("---importorskip")

# @pytest.importorskip("requests", minversion="2.26.0")
# def test_case13():
#     print("---importorskip")