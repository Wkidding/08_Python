# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/25 15:44
@File   ：test_dependency
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 依赖执行pytest-dependency
"""
import pytest


# # 执行时，test_create_order 仅在 test_login 成功执行后才会运行。
# # 若 test_login 失败，test_create_order 将被跳过。
# @pytest.mark.dependency()                      # 声明为可被依赖
# def test_login():
#     assert False
#
# @pytest.mark.dependency(depends=["test_login"])  # 依赖 test_login
# def test_create_order():
#     assert True
#


# @pytest.mark.dependency()
# def test_a():
#     assert True
#
# @pytest.mark.dependency()
# def test_b():
#     assert True
#
# # 依赖 test_a 和 test_b，两者都成功才会执行
# @pytest.mark.dependency(depends=["test_a", "test_b"])
# def test_c():
#     assert True
#
# # 依赖 test_c，如果 test_c 被跳过，test_d 也会被跳过
# @pytest.mark.dependency(depends=["test_c"])
# def test_d():
#     assert True



# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#     assert False
#
# @pytest.mark.dependency()
# def test_b():
#     pass
#
# @pytest.mark.dependency(depends=["test_a"])
# def test_c():
#     pass
#
# @pytest.mark.dependency(depends=["test_b"])
# def test_d():
#     pass
#
# @pytest.mark.dependency(depends=["test_b", "test_c"])
# def test_e():
#     pass




@pytest.mark.dependency(name="a")
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False

@pytest.mark.dependency(name="b")
def test_b():
    pass

@pytest.mark.dependency(name="c", depends=["a"])
def test_c():
    pass

@pytest.mark.dependency(name="d", depends=["b"])
def test_d():
    pass

@pytest.mark.dependency(name="e", depends=["b", "c"])
def test_e():
    pass


# class TestOrder:
#     @pytest.mark.dependency()
#     def test_login(self):
#         assert True
#
#     # 依赖同类的 test_login，需使用 "TestOrder::test_login" 格式
#     @pytest.mark.dependency(depends=["TestOrder::test_login"])
#     def test_create_order(self):
#         assert True



class TestOrder:
    @pytest.mark.dependency(name="login")
    def test_login(self):
        assert True

    @pytest.mark.dependency(name="create_order", depends=["login"])
    def test_create_order(self):
        assert True


@pytest.mark.dependency()  # 类级别标记，所有方法均可被依赖
class TestAPI:
    def test_login(self):
        assert True

    def test_logout(self):
        assert True