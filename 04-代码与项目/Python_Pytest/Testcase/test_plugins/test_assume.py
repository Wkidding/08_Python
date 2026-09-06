# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/25 16:34
@File   ：test_assume
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 多重校验pytest-assume
"""

import pytest

def test_assume():
    pytest.assume(1 == 1)      # 成功
    pytest.assume(1 == 2)      # 失败，但继续执行
    pytest.assume(2 == 2)      # 成功
    pytest.assume(2 == 3)      # 失败，但继续执行
    print("测试完成")           # 仍然会执行