# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/9 07:32
@File   ：test_08
@IDE    ：PyCharm
=================================================="""

import pytest

@pytest.mark.xfail
def test_case1 ( ):
    print("代码开发中")
    assert 1 == 1

@pytest.mark.xfail
def test_case_02():
    print("代码开发中")
    assert 1==2

@pytest.mark.xfail(1==1, reason="代码开发中")
def test_case_03():
    print("---xfail")
    assert 1==1

@pytest.mark.xfail(1==2, reason="代码开发中")
def test_case_04():
    print("---xfail")
    assert 1==1


def test_case_05():
    pytest.xfail("代码开发中")
    print("---xfail")
    assert 1 == 1


@pytest.mark.xfail(reason="当前环境没法测试")
class Test06:
    def test_06_b (self):
        print("---test_b")
        assert 1 == 1

    def test_06_a (self):
        print("---test_a")
        assert 1 == 2


# pytestmark = pytest.mark.xfail(reason="当前环境没法测试")
# class Test07:
#     def test_07_b (self):
#         print("---test_b")
#         assert 1 == 1
#
#     def test_07_a (self):
#         print("---test_a")
#         assert 1 == 2


@pytest.mark.xfail()
def test_09_c ( ):
    print("---test_c")
    assert 1 == 1

@pytest.mark.xfail(run=True)
def test_09_b ( ):
    print("---test_b")
    assert 1 == 1

@pytest.mark.xfail(run=False)
def test_09_a ( ):
    print("---test_a")
    raise Exception("异常")


@pytest.mark.xfail
def test_10_d ( ):
    print("---test_d")
    raise Exception("异常")

@pytest.mark.xfail(reason="异常了")
def test_10_c ( ):
    print("---test_c")
    raise Exception("异常")

@pytest.mark.xfail(raises=RuntimeError)
def test_10_b ( ):
    print("---test_b")
    raise RuntimeError("运行时异常")

# @pytest.mark.xfail(raises=RuntimeError)
# def test_10_a ( ):
#     print("---test_a")
#     raise Exception("异常")


@pytest.mark.xfail
def test_11_f ( ):
    print("---test_f")
    assert 1 == 1

@pytest.mark.xfail
def test_11_e ( ):
    print("---test_e")
    assert 1 == 2

@pytest.mark.xfail(strict=False)
def test_11_d ( ):
    print("---test_d")
    assert 1 == 1

@pytest.mark.xfail(strict=False)
def test_11_c ( ):
    print("---test_c")
    assert 1 == 2

@pytest.mark.xfail(strict=True)
def test_11_b ( ):
    print("---test_b")
    assert 1 == 1

@pytest.mark.xfail(strict=True)
def test_11_a ( ):
    print("---test_a")
    assert 1 == 2