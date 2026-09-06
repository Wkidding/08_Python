# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/20 06:36
@File   ：test_22
@IDE    ：PyCharm
=================================================="""
"""
parametrize参数化 与 Fixture 结合使用
"""

import pytest

@pytest.fixture
def processed_data(request):
    # request.param 接收 parametrize 传递的值
    raw = request.param
    return raw * 2  # 预处理：乘以2

@pytest.mark.parametrize("processed_data", [1, 2, 3, 4], indirect=True)
def test_processed(processed_data):
    print(f"Processed: {processed_data}")
    # 输出: 2, 4, 6, 8




@pytest.fixture
def factor(request):
    return request.param

@pytest.fixture
def number(request):
    return request.param

@pytest.mark.parametrize("factor", [2, 3], indirect=True)
@pytest.mark.parametrize("number", [10, 20], indirect=True)
def test_multiply(number, factor):
    result = number * factor
    print(f"{number} × {factor} = {result}")
    # 生成 4 个测试：
    # 10×2, 20×2, 10×3, 20×3




def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

@pytest.mark.parametrize("input_text,expected", [
    ("hello world", "Hello World"),
    ("python testing", "Python Testing"),
    ("", ""),
    ("single", "Single"),
    ("multiple   spaces", "Multiple   Spaces")  # 保留多个空格
])
def test_capitalize_words(input_text, expected):
    assert capitalize_words(input_text) == expected





def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5)
])
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("a,b", [
    (10, 0),
    (5, 0),
    (0, 0)
])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, b)
