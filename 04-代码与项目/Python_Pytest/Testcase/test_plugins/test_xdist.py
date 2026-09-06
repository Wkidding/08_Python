# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/25 14:59
@File   ：test_xdist
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - 并发执行pytest-xdist
"""

import pytest

class Test01:
    def test_d (self):
        print("--test_d")

    @pytest.mark.run(order=-3)
    def test_c (self):
        print("--test_c")

    @pytest.mark.run(order=0)
    def test_b (self):
        print("--test_b")

    @pytest.mark.run(order=1)
    def test_a (self):
        print("--test_a")



class Test02:
    @pytest.mark.xdist_group(name="database")
    def test_db_connection(self):
        print("数据库连接测试")

    @pytest.mark.xdist_group(name="database")
    def test_db_query(self):
        print("数据库查询测试")

    @pytest.mark.xdist_group(name="api")
    def test_api_login(self):
        print("API 登录测试")