# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/10 07:30
@File   ：test_11
@IDE    ：PyCharm
=================================================="""
"""
assert断言
"""

import pytest
import warnings
# def test_01_1_x():
#     assert True
# def test_01_2_x():
#     assert 'fsdkgitndcsdf'
# def test_01_3_in():
#     assert 'cs' in 'fsdkgitndcsdf'
# def test_01_4_not():
#     assert not True


# def test_02_1_num():
#     assert 1 == 1
# def test_02_2_str():
#     assert "1" == "1"
# def test_02_3_dic():
#     assert {"name": "ren"} == {"name": "qzcsbj"}, "---fail"
# def test_02_4_list():
#     assert [1, 2] == [1, 2], "---fail"
# def test_02_5_tuple():
#     assert (1, 2) == (1, 3)


# @pytest.mark.xfail
# def test_03_d():
#     print("---test_d")
#     raise Exception("异常")
#
# @pytest.mark.xfail(reason="异常了")
# def test_03_c():
#     print("---test_c")
#     raise Exception("异常")
# @pytest.mark.xfail(raises=RuntimeError)
# def test_03_b():
#     print("---test_b")
#     raise RuntimeError("运行时异常")
#
# @pytest.mark.xfail(raises=RuntimeError)
# def test_03_a():
#     print("---test_a")
#     raise Exception("异常")


# def test_04_a():
#     # 捕获特定异常；采用pytest.raises上下文管理预期异常
#     # 哪怕with下面的代码发生了ZeroDivisionError类型的异常，整个用例不会认为是异常用例，认为是正常的
#     with pytest.raises(ZeroDivisionError):
#         1 / 0
#
# def test_04_b():
#     #  可以捕获异常，获取细节（异常类型、异常信息），后面使用
#     #  下面通过ex来访问异常信息
#     with pytest.raises(ZeroDivisionError) as ex:
#         1 / 0
#     print("---ex:",ex.value)
#     # 断言异常value值
#     assert "division" in str(ex.value)
#     # 断言异常类型
#     assert ex.type == ZeroDivisionError
#
# def test_04_c():
#     # 用正则匹配异常信息
#     with pytest.raises(ZeroDivisionError, match=".*division.*") as ex:
#         1 / 0
#     pass


# 下面写法，产生的警告不会打印出来
def test_warning_assert ( ):
    with pytest.warns(UserWarning):
        warnings.warn("自定义警告1", UserWarning)


# 可以使用record获取警告信息
def test_warning_assert2 ( ):
    with pytest.warns(RuntimeWarning) as record:
        warnings.warn("自定义警告2", RuntimeWarning)
    assert len(record) == 1
    assert record[0].message.args[0] == "自定义警告2"


# match通过正则匹配异常信息中的关键字
def test_warning_assert3 ( ):
    with pytest.warns(UserWarning, match=".*自定义.*3"):
        warnings.warn("自定义警告3", UserWarning)