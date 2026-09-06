# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/18 16:04
@File   ：test_19
@IDE    ：PyCharm
=================================================="""
"""
fixture 对用例重命名
"""

import pytest

@pytest.fixture(params=['a', 'b', 'c'])
def fun_01(request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

class Test01:
    def test_case_01(self, fun_01):
        print(f"---test_case_01，data={fun_01}")




data = ['a', 'b', 'c']
data2 = [1, 2, 3]

@pytest.fixture(params=data)
def fun_02_01(request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

@pytest.fixture(params=data2)
def fun_02_02(request):
    return request.param

class Test02:
    def test_case_02(self, fun_02_01, fun_02_02):
        print(f"---test_case_02，data={fun_02_01},{fun_02_02}")


@pytest.fixture(params=data, ids=['role1','role2','role2'])
def fun_03_01(request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

@pytest.fixture(params=data2, ids=['user','product','stock'])
def fun_03_02(request):
    return request.param

class Test03:
    def test_case_03(self, fun_03_01, fun_03_02):
        print(f"---test_case，data={fun_03_01},{fun_03_02}")


data04 = ['product1', 'product2', 'product3']

@pytest.fixture(params=data04, ids=['add product success', 'add product fail', 'update product success'])
def fun_04 (request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

class Test04:
    def test_case_04 (self, fun_04):
        print(f"---test_case_04，data={fun_04}")


data05 = ['product1', 'product2', 'product3']

@pytest.fixture(params=data05, ids=['add product success', 'add product fail'])
def fun_05 (request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

class Test05:
    def test_case_05 (self, fun_05):
        print(f"---test_case_05，data={fun_05}")




data06 = ['product1', 'product2', 'product3']

@pytest.fixture(params=data06, ids=['add product success','add product fail','update product success'], name="product")
def fun_06(request):  # 必须是request这个参数名
    return request.param  # 依次取列表中的每个值返回

class Test06:
    def test_case_06(self, product):
        print(f"---test_case_06，data={product}")