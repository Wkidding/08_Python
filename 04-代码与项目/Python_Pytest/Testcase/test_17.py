# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/16 06:26
@File   ：test_17
@IDE    ：PyCharm
=================================================="""
"""
fixture标志传参
"""
import pytest

@pytest.fixture
def fun_01 (request):
    marker = request.node.get_closest_marker("mydata")
    if marker is None:
        data = None
    else:
        data = marker.args[0] + 1
    return data

@pytest.mark.mydata(1)
def test_data_01 (fun_01):
    print("fun_01={}".format(fun_01))

"""
测试：不同传参方式
"""
@pytest.fixture
def process_marker(request):
    marker = request.node.get_closest_marker("mydata")
    return marker

# 方式1：单个参数
@pytest.mark.mydata(10)
def test_single(process_marker):
    print(process_marker.args[0])  # 输出: 10

# 方式2：多个参数
@pytest.mark.mydata(10, 20, 30)
def test_multiple(process_marker):
    print(process_marker.args)  # 输出: (10, 20, 30)
    print(process_marker.args[1])  # 输出: 20

# 方式3：关键字参数
@pytest.mark.mydata(a=1, b=2, c=3)
def test_kwargs(process_marker):
    print(process_marker.kwargs)  # 输出: {'a': 1, 'b': 2, 'c': 3}
    print(process_marker.kwargs["b"])  # 输出: 2

# 方式4：混合使用
@pytest.mark.mydata(100, x=200, y=300)
def test_mixed(process_marker):
    print(process_marker.args)     # 输出: (100,)
    print(process_marker.kwargs)   # 输出: {'x': 200, 'y': 300}
    print(process_marker.args[0] + process_marker.kwargs["x"])  # 输出: 300


"""
测试：标记的继承与覆盖
覆盖规则：方法级别标记 > 类级别标记 > 模块级别标记 > 全局标记
"""
@pytest.fixture
def get_marker (request):
    return request.node.get_closest_marker("mydata")

# 类级别的标记
@pytest.mark.mydata(111)
class TestClass:

    # 方法级别的标记会覆盖类级别的
    @pytest.mark.mydata(222)
    def test_method_1 (self, get_marker):
        print(get_marker.args[0])  # 输出: 222（方法标记覆盖类标记）

    # 没有方法级别标记时，使用类级别的
    def test_method_2 (self, get_marker):
        print(get_marker.args[0])  # 输出: 111（继承类标记）

    # 多个标记可以叠加
    @pytest.mark.mydata(333)
    @pytest.mark.another(555)
    def test_method_3 (self, get_marker):
        print(get_marker.args[0])  # 输出: 333


"""
测试：标记不存在时的处理
"""
@pytest.fixture
def safe_marker(request):
    marker = request.node.get_closest_marker("mydata")
    if marker is None:
        return 0  # 默认值
    return marker.args[0]

# 没有标记
def test_no_marker(safe_marker):
    print(safe_marker)  # 输出: 0（使用默认值）

# 有标记
@pytest.mark.mydata(10)
def test_with_marker(safe_marker):
    print(safe_marker)  # 输出: 10


"""
测试：复杂传参
"""
@pytest.fixture
def fun_02 (request):
    marker = request.node.get_closest_marker("mydata")
    if marker is None:
        data = None
    else:
        data = marker.args[0]
        data[-1] = 666
    return data

@pytest.mark.mydata([1, 2, 3])
def test_data_02 (fun_02):
    print("fun={}".format(fun_02))


"""
测试：传入多个参数
"""
@pytest.fixture
def fun_03 (request):
    marker = request.node.get_closest_marker("mydata")
    marker2 = request.node.get_closest_marker("mydata2")
    if marker is None:
        data = None
    else:
        data = marker.args[0]
        data[-1] = 666
    if marker2 is None:
        data2 = None
    else:
        data2 = marker2.args[0] + 1
    return data, data2

@pytest.mark.mydata([1, 2, 3])
@pytest.mark.mydata2(1)
def test_data_03 (fun_03):
    print("fun_03={}".format(fun_03))



if __name__ == '__main__':
    pytest.main(['-vs'])
