# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/20 06:32
@File   ：test_21
@IDE    ：PyCharm
=================================================="""
"""
 parametrize参数化: 模块级别参数化 
"""
import pytest

pytestmark = pytest.mark.parametrize("env", ["dev", "test", "prod"])

def test_config(env):
    print(f"Testing environment: {env}")
    assert env in ["dev", "test", "prod"]