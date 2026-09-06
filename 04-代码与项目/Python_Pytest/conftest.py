# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/15 07:39
@File   ：conftest
@IDE    ：PyCharm
=================================================="""
"""
全局conftest.py,配置管理共享的fixture
"""
import pytest

# @pytest.fixture(autouse=True, scope="function")
# def f():
#     print("---fixture : function-前")
#     yield
#     print("---fixture : function-后")
#
# @pytest.fixture(autouse=True, scope="class")
# def f2():
#     print("---fixture : class-前")
#     yield
#     print("---fixture : class-后")
#
# @pytest.fixture(autouse=True, scope="module")
# def f3():
#     print("---fixture : module-前")
#     yield
#     print("---fixture : module-后")
#
# @pytest.fixture(autouse=True, scope="package")
# def f4():
#     print("---fixture : package-前")
#     yield
#     print("---fixture : package-后")
#
# @pytest.fixture(autouse=True, scope="session")
# def f5():
#     print("---fixture : session-前")
#     yield
#     print("---fixture : session-后")


# @pytest.fixture(autouse=False, scope="function")
# def f0():
#     print("---fixture : function-前（全局f0）")
#     yield
#     print("---fixture : function-后（全局f0）")