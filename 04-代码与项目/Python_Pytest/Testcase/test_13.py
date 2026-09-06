# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/12 15:33
@File   ：tese_13
@IDE    ：PyCharm
=================================================="""
from sqlalchemy.sql import True_

"""
fixture 简介&调用
"""
import pytest

# 定义 fixture
@pytest.fixture()
def fun_01_01():
    print("--fun_01_01()中fixture")

# 定义 fixture
@pytest.fixture()
def fun_01_02 ( ):
    print("--fun_01_02()中fixture2")

# 测试函数使用 fixture（通过参数名注入），即“函数引用”
def test_01_a (fun_01_01):
    print("--------------test_01_a")

class Test01:
    # 函数引用：引用的方法是在 本测试类外 被fixture标记的方法。
    def test_01_b (self, fun_01_02):
        print("--------------test_01_b")

    # 测参数引用：引用的方法是在 本测试类中 被fixture标记的方法。
    def test_01_c (self, fun_01_03):
        print("--------------test_01_c")

    @pytest.fixture()
    def fun_01_03 (self):
        print("--fun_01_03()中fixture3")






@pytest.fixture()
def fun_02_01 ( ):
    print("--fun_02_01 中的 fixture")

@pytest.fixture()
def fun_02_02 ( ):
    print("--fun_02_02 中的 fixture2")

# 先执行fun_02_01 中的 fixture，在执行本测试用例中的内容
def test_02_a (fun_02_01):
    print("--------------test_02_a")

class Test02:
    # 先执行fun_02_01 中的 fixture，在执行本测试用例中的内容
    def test_02_b (self, fun_02_01):
        print("--------------test_02_b")

    # 先执行fun_02_02 中的 fixture，再执行执行fun_02_01 中的 fixture，最后执行本测试用例中的内容
    @pytest.mark.usefixtures('fun_02_02', 'fun_02_01')
    def test_02_c (self):
        print("--------------test_02_c")






@pytest.fixture()
def fun_03_1():
    print("--fun_03_1 fixture")

@pytest.fixture()
def fun_03_2():
    print("--fun_03_2 fixture2")

def test_03_a (fun_03_1):
    print("--------------test_03_a")

@pytest.mark.usefixtures('fun_03_1')
@pytest.mark.usefixtures('fun_03_2')
class Test03:
    def test_03_b (self):
        print("--------------test_03_b")

    def test_03_c (self):
        print("--------------test_03_c")






@pytest.fixture()
def fun_04_01():
    print("--fun_04_01 fixture")

@pytest.fixture()
def fun_04_02():
    print("--fun_04_02 fixture2")

def test_04_a(fun_04_01):
    print("--------------test_04_a")

class Test04:
    def test_04_b(self):
        print("--------------test_04_b")

    @pytest.mark.usefixtures('fun_04_01')
    def test_04_c(self, fun_04_02):
        print("--------------test_04_c")






@pytest.fixture()
def fun_05_01 ( ):
    print("--fun_05_01 fixture")

@pytest.fixture()
def fun_05_02 ( ):
    print("--fun_05_02 fixture2")

def test_05_a (fun_05_01):
    print("--------------test_05_a")

@pytest.mark.usefixtures('fun_05_01')
class Test05:
    def test_05_b (self):
        print("--------------test_05_b")

    def test_05_c (self, fun_05_02):
        print("--------------test_05_c")






@pytest.fixture()
def fun_06_01():
    print("--fun_06_01 fixture")

@pytest.fixture()
def fun_06_02():
    print("--fun_06_02 fixture2")

def test_06_a(fun_06_01):
    print("--------------test_06_a")

@pytest.mark.usefixtures('fun_06_02')
class Test06:
    def test_06_b (self):
        print("--------------test_06_b")

    @pytest.mark.usefixtures('fun_06_01')
    def test_06_c (self):
        print("--------------test_06_c")






@pytest.fixture()
def fun_07_01 ( ):
    print("--fun_07_02 fixture")

# 防止后续用例引用fun_07_02，先注释（运行时需要放开注释）
# @pytest.fixture(autouse=True)
def fun_07_02 ( ):
    print("--fun_07_02 fixture2")

def test_07_a ( ):
    print("--------------test_a")

class Test07:
    def test_07_b (self):
        print("--------------test_b")

    def test_07_c (self):
        print("--------------test_c")






@pytest.fixture()
def fun_08_01():
    print("---fun_08_01")

@pytest.fixture()
def fun_08_02(fun_08_01):
    print("---fun_08_02")

def test_08_a(fun_08_02):
    print("--------------test_08_a")

# 下面写法报错
"""
❌  1、错误嵌套：不能使用usefixtures标记来嵌套不同的fixture
"""
# @pytest.fixture()
# def fun_08_01 ( ):
#     print("---fun_08_01")
#
# @pytest.fixture()
# @pytest.mark.usefixtures(fun_08_01)
# def fun_08_02():
#     print("---fun_08_02")


# 错误用法，报错
"""
❌ 错误：2、错误用法：@pytest.mark.usefixtures() 接收的是 fixture 的名称（字符串），而不是 fixture 函数本身。
"""
# @pytest.fixture()
# def fun_08_01():
#     print("---fun_08_01")
#
# @pytest.fixture()
# def fun_08_02(fun_08_01):
#     print("---fun_08_02")
#
# @pytest.mark.usefixtures(fun_08_02)
# def test_08_a():
#     print("--------------test_08_a")



