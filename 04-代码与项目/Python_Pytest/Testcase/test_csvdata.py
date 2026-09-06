# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/22 06:45
@File   ：test_csvdata
@IDE    ：PyCharm
=================================================="""
"""
pytest 使用parameter参数化获取csv文件数据进行测试
"""

import pytest
import csv
import os

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_data_from_csv (file_path):
    item = []
    c = csv.reader(open(file_path, "r", encoding='utf-8'))
    for i in c:
        item.append(i)
    print(f"返回的参数：{item}")
    return item

@pytest.mark.parametrize("param", read_data_from_csv(BASE_PATH + "/data/case.csv"))
def test_case (param):
    print(f"uname={param[0]}, pwd={param[1]}")