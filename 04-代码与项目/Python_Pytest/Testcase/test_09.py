# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/10 06:25
@File   ：test_09
@IDE    ：PyCharm
=================================================="""

"""
pytest中配置过滤警告
"""
import pytest
import warnings


def test_01_a ( ):
    print("---test_01_a")
    assert fun_01() == 1

def fun_01():
    print("---fun")
    warnings.warn(UserWarning("自定义warning"))
    return 1


def test_02_b():
    print("---est_02_b")
    warnings.warn(UserWarning("自定义warning"))
    assert 1 == 1

def test_02_a ( ):
    print("---test_02_a")
    assert fun_02() == 1

def fun_02 ( ):
    print("---fun")
    warnings.warn(UserWarning("自定义warning"))
    warnings.warn(UserWarning("自定义warning"))
    return 1


@pytest.mark.filterwarnings("ignore:.*自定义.*")
def test_03_a ():
    print("---test_a")
    assert fun_03() == 1

def fun_03 ():
    print("---fun_03")
    warnings.warn(UserWarning("自定义warning"))
    return 1


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_04_a():
    print("---test_04_a")
    assert fun_04() == 1

def fun_04():
    print("---fun_04")
    warnings.warn(UserWarning("自定义warning"))
    return 1


@pytest.mark.filterwarnings("ignore:自定义")
class Test05:
    def test_05_a (self):
        print("---test_05_a")
        assert self.fun_05() == 1

    def fun_05 (self):
        print("---fun_05")
        warnings.warn(UserWarning("自定义warning"))
        return 1



pytestmark = pytest.mark.filterwarnings("ignore")
class Test06:
    def test_06_a (self):
        print("---test_06_a")
        assert self.fun_06() == 1

    def fun_06(self):
        print("---fun_06")
        warnings.warn(UserWarning("自定义warning"))
        return 1