# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/17 06:21
@File   ：test_18
@IDE    ：PyCharm
=================================================="""
"""
fixture返回值实现参数化
"""

import pytest


@pytest.fixture
def fun_01():
    return 666

class Test01:
    def test_case_01 (self, fun_01):
        print("---test_case_01")
        print(f"data={fun_01}")






"""
错误用法：不能直接使用usefixtures调用已经参数化的fixture
"""
# @pytest.fixture
# def fun_02():
#     return 999
#
# @pytest.mark.usefixtures("fun_02")
# class Test02:
#     def test_case_02 (self):
#         print("---test_case_02")
#         print(f"data={fun_02}")


"""
fixture实现参数化的方式
"""
@pytest.fixture(params=[1, 2, 3, 4])
def number(request):
    return request.param  # # request.param 会自动遍历 params 列表的每个元素,依次返回 1, 2, 3, 4

# 测试函数会被执行 4 次，每次传入不同的参数
def test_numbers(number):
    print(f"number={number}")
    assert number > 0





@pytest.fixture(params=[
    (1, 2, 3),
    (4, 5, 9),
    (7, 8, 15)
])
def tuple_data(request):
    return request.param  # 返回元组

def test_tuple(tuple_data):
    a, b, c = tuple_data
    assert a + b == c
    print(f"{a} + {b} = {c}")




@pytest.fixture(params=[
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
])
def dict_data(request):
    return request.param  # 返回字典

def test_dict(dict_data):
    print(f"User: {dict_data['name']}, Age: {dict_data['age']}")
    assert dict_data["age"] >= 18





class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@pytest.fixture(params=[
    User("Alice", 25),
    User("Bob", 30),
    User("Charlie", 35)
])
def user_define_obj(request):
    return request.param

def test_user_define_obj(user_define_obj):
    print(f"User: {user_define_obj.name}, Age: {user_define_obj.age}")
    assert user_define_obj.age >= 18





# fixture 定义一个参数名
@pytest.fixture
def test_data(request):
    return request.param  # 接收 parametrize 传递的值

# 使用 indirect=True，让 parametrize 的值传给 fixture
# 注意：使用parametrize标记传fixture要加双引号
@pytest.mark.parametrize("test_data", [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
], indirect=True)
def test_user(test_data):
    print(f"User: {test_data['name']}, Age: {test_data['age']}")
    assert test_data["age"] >= 18





@pytest.fixture(params=[1, 2])
def a(request):
    return request.param

@pytest.fixture(params=[3, 4])
def b(request):
    return request.param

def test_multiply(a, b):
    result = a * b
    print(f"{a} × {b} = {result}")
    # 执行 2×2=4 次
    # 1×3, 1×4, 2×3, 2×4





@pytest.fixture(params=["username", "email"])
def login_field(request):
    return request.param

@pytest.fixture(params=[
    {"valid": True, "value": "correct"},
    {"valid": False, "value": "wrong"}
])
def credential(request):
    return request.param

def test_login(login_field, credential):
    print(f"Field: {login_field}, Credential: {credential}")
    # 2×2=4 种组合






def generate_params():
    """动态生成参数列表"""
    params = []
    for i in range(10):
        params.append({"id": i, "value": i * 2})
    return params

@pytest.fixture(params=generate_params())
def dynamic_data(request):
    return request.param

def test_dynamic(dynamic_data):
    print(f"ID: {dynamic_data['id']}, Value: {dynamic_data['value']}")
    assert dynamic_data["value"] == dynamic_data["id"] * 2





@pytest.fixture(params=[1, 2, 3])
def processed_data(request):
    # 对参数进行预处理
    raw = request.param
    return {
        "original": raw,
        "squared": raw ** 2,
        "cubed": raw ** 3
    }

def test_processed(processed_data):
    print(f"Original: {processed_data['original']}")
    print(f"Squared: {processed_data['squared']}")
    print(f"Cubed: {processed_data['cubed']}")
    assert processed_data["squared"] == processed_data["original"] ** 2
    assert processed_data["cubed"] == processed_data["original"] ** 3


@pytest.fixture(params=[1, 2, 3])
def number_with_marker (request):
    # 获取测试函数上的标记
    marker = request.node.get_closest_marker("multiplier")
    multiplier = marker.args[0] if marker else 1

    # 参数化数据 × 标记数据
    return request.param * multiplier

@pytest.mark.multiplier(10)
def test_with_marker (number_with_marker):
    print(f"Result: {number_with_marker}")
    # 输出: 10, 20, 30






"""
在yeild中返回params中的值
"""
@pytest.fixture(params=['111', '222', '333', '444', '555'])
def fun_03 (request):  # 必须是request这个参数名
    print("---前置")
    yield request.param  # 依次取列表中的每个值返回
    print("---后置")

class Test03:
    def test_case (self, fun_03):
        print(f"---test_case，data={fun_03}")