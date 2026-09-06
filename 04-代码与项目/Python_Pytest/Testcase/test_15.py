# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/14 07:03
@File   ：test_15
@IDE    ：PyCharm
=================================================="""
"""
fixture作用域(scope)详解
"""

import pytest


@pytest.fixture(autouse=True)
def fun_01():
    print("---fun_01 fixture")

def test_01_a():
    print("--------------test_01_a")

class Test01:
    def test_01_b (self):
        print("--------------test_01_b")

    def test_01_c (self):
        print("--------------test_01_c")





@pytest.fixture(autouse=True, scope="function")
def fun_02_1():
    print("--fun_02_1 fixture : function-前")
    yield
    print("--fun_02_1 fixture : function-后")

@pytest.fixture(autouse=True, scope="class")
def fun_02_2():
    print("--fun_02_2 fixture : class-前")
    yield
    print("--fun_02_2 fixture : class-后")

@pytest.fixture(autouse=True, scope="module")
def fun_02_3():
    print("--fun_02_3 fixture : module-前")
    yield
    print("--fun_02_3 fixture : module-后")

@pytest.fixture(autouse=True, scope="package")
def fun_02_4():
    print("--fun_02_4 fixture : package-前")
    yield
    print("--fun_02_4 fixture : package-后")

@pytest.fixture(autouse=True, scope="session")
def fun_02_5():
    print("--fun_02_5 fixture : session-前")
    yield
    print("--fun_02_5 fixture : session-后")

def test_02_a():
    print("--------------test_02_a")

def test_02_b():
    print("--------------test_02_b")

class Test02Scope:
    def test_02_c (self):
        print("--------------test_02_c")

    def test_02_d (self):
        print("--------------test_02_d")





def test_03_a ():
    print("--------------test_03_a")

def test_03_b ():
    print("--------------test_03_b")

class Test03Scope:
    def test_03_c (self):
        print("--------------test_03_c")

    def test_03_d (self):
        print("--------------test_03_d")

    @pytest.fixture(autouse=True, scope="function")
    def fun_03_01 (self):
        print("---fixture : function-前")
        yield
        print("---fixture : function-后")

    @pytest.fixture(autouse=True, scope="class")
    def fun_03_02 (self):
        print("---fixture : class-前")
        yield
        print("---fixture : class-后")

    @pytest.fixture(autouse=True, scope="module")
    def fun_03_03 (self):
        print("---fixture : module-前")
        yield
        print("---fixture : module-后")

    @pytest.fixture(autouse=True, scope="package")
    def fun_03_04 (self):
        print("---fixture : package-前")
        yield
        print("---fixture : package-后")

    @pytest.fixture(autouse=True, scope="session")
    def fun_03_05 (self):
        print("---fixture : session-前")
        yield
        print("---fixture : session-后")





def test_04_a ():
    print("--------------test_04_a")

def test_04_b():
    print("--------------test_04_b")

@pytest.fixture(autouse=True, scope="function")
def fun_04_01():
    print("---fixture : function-前")
    yield
    print("---fixture : function-后")

@pytest.fixture(autouse=True, scope="class")
def fun_04_02():
    print("---fixture : class-前")
    yield
    print("---fixture : class-后")

@pytest.fixture(autouse=True, scope="module")
def fun_04_03():
    print("---fixture : module-前")
    yield
    print("---fixture : module-后")

@pytest.fixture(autouse=True, scope="package")
def fun_04_04():
    print("---fixture : package-前")
    yield
    print("---fixture : package-后")

@pytest.fixture(autouse=True, scope="session")
def fun_04_05():
    print("---fixture : session-前")
    yield
    print("---fixture : session-后")

class Test04Scope:
    def test_04_c (self):
        print("--------------test_04_c")

    def test_04_d (self):
        print("--------------test_04_d")

    @pytest.fixture(autouse=True, scope="function")
    def fun_04_01 (self):
        print("---fixture : function-前(类中)")
        yield
        print("---fixture : function-后(类中)")

    @pytest.fixture(autouse=True, scope="class")
    def fun_04_02 (self):
        print("---fixture : class-前(类中)")
        yield
        print("---fixture : class-后(类中)")

    @pytest.fixture(autouse=True, scope="module")
    def fun_04_03 (self):
        print("---fixture : module-前(类中)")
        yield
        print("---fixture : module-后(类中)")

    @pytest.fixture(autouse=True, scope="package")
    def fun_04_04 (self):
        print("---fixture : package-前(类中)")
        yield
        print("---fixture : package-后(类中)")

    @pytest.fixture(autouse=True, scope="session")
    def fun_04_05 (self):
        print("---fixture : session-前(类中)")
        yield
        print("---fixture : session-后(类中)")