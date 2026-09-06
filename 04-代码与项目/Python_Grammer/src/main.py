# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2024/5/26 13:56
@File   ：main
@IDE    ：PyCharm
=================================================="""

from collections.abc import Iterable, Iterator
import sys

import time

from xdist.plugin import pytest_addhooks


def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"尝试 {attempt+1} 失败: {e}")
                    time.sleep(delay)
            raise Exception("所有尝试均失败")
        return wrapper
    return decorator

@retry(3, delay=1)
def unstable_network_call():
    # 模拟可能失败的操作
    pass