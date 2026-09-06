# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/22 07:02
@File   ：test_reruns
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 失败重试pytest-rerunfailures
"""
import pytest
import sys

def test_b ( ):
    print("---test_b")
    assert 1 == 1


def test_a ( ):
    print("---test_a")
    assert 1 == 2



# @pytest.mark.flaky(reruns=5)
@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_example(request):
    print("--通过用例")
    assert 1 == 1
    print("--失败用例")
    assert 1 == 2



# 仅在特定条件下启用重试
@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32"))
def test_windows_only():
    pass



# 只对 AssertionError 和 ValueError 进行重试
@pytest.mark.flaky(reruns=5, only_rerun=["AssertionError", "ValueError"])
def test_specific_errors():
    print("--失败用例")
    assert 1 == 2

# 排除 AssertionError，其他错误均重试
@pytest.mark.flaky(reruns=5, rerun_except="AssertionError")
def test_except_errors():
    print("--失败用例")
    assert 1 == 2