# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/18 17:06
@File   ：test_20
@IDE    ：PyCharm
=================================================="""
"""

"""

import pytest
## 测试方法形参名要和parametrize里面的参数一样
@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_greeting(name):
    assert len(name) > 0
    print(f"Hello, {name}!")





# 修饰器放在函数上，参数值为基本类型（int/str/bool等）
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30)
])
def test_add(a, b, expected):
    """测试加法运算"""
    result = a + b
    assert result == expected

# 字符串示例
@pytest.mark.parametrize("username, password", [
    ("admin", "123456"),
    ("user1", "abc123"),
    ("guest", "guest123")
])
def test_login(username, password):
    """测试登录功能"""
    print(f"用户名: {username}, 密码: {password}")
    assert len(username) > 0
    assert len(password) >= 6


## 1.使用字典作为参数值，数据更结构化
@pytest.mark.parametrize("user_info", [
    { "name": "张三", "age": 25, "city": "北京" },
    { "name": "李四", "age": 30, "city": "上海" },
    { "name": "王五", "age": 28, "city": "深圳" }
])
def test_user_info (user_info):
    """测试用户信息验证"""
    # 通过字典key访问数据
    name = user_info["name"]
    age = user_info["age"]
    city = user_info["city"]

    print(f"姓名: {name}, 年龄: {age}, 城市: {city}")

    # 断言验证
    assert name is not None
    assert 0 < age < 150
    assert city in ["北京", "上海", "深圳", "广州"]


## 2.更复杂的字典结构（嵌套）
@pytest.mark.parametrize("order", [
    {
        "order_id": "ORD001",
        "customer": { "name": "张三", "phone": "13800138001" },
        "items": [{ "name": "苹果", "price": 5.0 }],
        "total": 5.0
    },
    {
        "order_id": "ORD002",
        "customer": { "name": "李四", "phone": "13800138002" },
        "items": [{ "name": "香蕉", "price": 3.0 }, { "name": "橙子", "price": 4.0 }],
        "total": 7.0
    }
])
def test_order_processing (order):
    """测试订单处理"""
    # 访问嵌套字典数据
    assert order["order_id"].startswith("ORD")
    assert order["customer"]["phone"].startswith("138")
    assert len(order["items"]) > 0

    # 计算总价验证
    calculated_total = sum(item["price"] for item in order["items"])
    assert calculated_total == order["total"]


# 将参数化修饰器放在测试类上
@pytest.mark.parametrize("a, b", [
    (10, 20),
    (100, 200),
    (1, 99)
])
class TestMathOperations:
    """测试类级别的参数化"""
    def test_addition (self, a, b):
        """测试加法 - 自动接收类级别的参数"""
        result = a + b
        print(f"加法测试: {a} + {b} = {result}")
        assert result > 0

    def test_multiplication (self, a, b):
        """测试乘法 - 自动接收类级别的参数"""
        result = a * b
        print(f"乘法测试: {a} * {b} = {result}")
        assert result > 0

    def test_comparison (self, a, b):
        """测试比较运算 - 自动接收类级别的参数"""
        # 注意：参数会依次传入每个测试方法
        assert a != b  # 使用 (10,20) 时，10 != 20 为 True
        # 但如果参数是 (10,10)，这个测试就会失败


# 测试类级别的参数化 - 所有方法共享参数
@pytest.mark.parametrize("username, password, expected", [
    ("admin", "admin123", True),
    ("user1", "pass123", True),
    ("invalid", "wrong", False)
])
class TestUserAuthentication:
    """用户认证测试 - 多个方法共享参数"""
    def test_validate_username (self, username, password, expected):
        """验证用户名格式"""
        # 用户名必须包含字母或数字
        is_valid = username.isalnum() or username == "admin"
        print(f"用户名验证: {username} -> {is_valid}")
        # 注意：这里使用expected来验证期望结果

    def test_password_strength (self, username, password, expected):
        """验证密码强度"""
        has_length = len(password) >= 6
        has_digit = any(c.isdigit() for c in password)
        has_letter = any(c.isalpha() for c in password)
        is_strong = has_length and (has_digit or has_letter)
        print(f"密码强度: {password} -> {is_strong}")

    def test_login_flow (self, username, password, expected):
        """测试完整的登录流程"""
        # 模拟登录验证
        login_result = self._mock_login(username, password)
        print(f"登录测试: {username}/{password} -> {login_result}")
        assert login_result == expected

    def _mock_login (self, username, password):
        """模拟登录验证逻辑"""
        valid_users = {
            "admin": "admin123",
            "user1": "pass123"
        }
        return valid_users.get(username) == password






data = [('韧','测试开发'),('全栈测试笔记','性能测试')]
@pytest.mark.parametrize("name,technology",data)
class Test01:
    def test_case(self, name, technology):
        print(f"name={name}, technology={technology}")





# @pytest.mark.parametrize(
#     "user,expected_age",
#     [
#         ({"name": "Alice", "age": 25}, 25),
#         ({"name": "Bob", "age": 30}, 30),
#         ({"name": "Charlie", "age": 35}, 35)
#     ],
#     ids=["Alice_25", "Bob_30", "Charlie_35"]
# )
# def test_user_age(user, expected_age):
#     assert user["age"] == expected_age

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        pytest.param("6*9", 42, marks=pytest.mark.xfail),  # 预期失败
        pytest.param("1/0", 0, marks=pytest.mark.skip(reason="避免除零错误"))
    ]
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected



@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_combination(x, y):
    print(f"x={x}, y={y}")


@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 4),
    (3, 6)
])
class TestMath:
    def test_double (self, n, expected):
        assert n * 2 == expected

    def test_add_one (self, n, expected):
        assert n + n == expected  # 也使用同样的参数

