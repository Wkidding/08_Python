# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/21 07:03
@File   ：test_24
@IDE    ：PyCharm
=================================================="""
"""
parameter 给用例取别名
"""

import pytest
from datetime import datetime, timedelta

## 方式1：
# 参数值列表
testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]

# 方式一： 通过 ids 列表指定别名
@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected





## 方式2：
# 方式二：使用 pytest.param 为每个用例单独指定 id
@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(
            datetime(2001, 12, 12),
            datetime(2001, 12, 11),
            timedelta(1),
            id="forward"  # 正向测试用例
        ),
        pytest.param(
            datetime(2001, 12, 11),
            datetime(2001, 12, 12),
            timedelta(-1),
            id="backward"  # 反向测试用例
        ),
        pytest.param(
            datetime(2001, 12, 12),
            datetime(2001, 12, 12),
            timedelta(0),
            id="same_time"  # 相同时间测试用例
        ),
    ]
)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected