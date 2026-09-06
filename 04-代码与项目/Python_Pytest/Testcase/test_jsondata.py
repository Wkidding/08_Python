# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/22 06:15
@File   ：test_jsondata
@IDE    ：PyCharm
=================================================="""
"""
pytest 使用parameter参数化获取json文件数据进行测试
"""
import pytest
import json
import os

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_data_from_json (file_path):
    data = { }
    with open(file_path, 'r', encoding="utf-8") as fp:
        data = json.load(fp)
    print(f"返回的参数：{data}")
    return data


@pytest.mark.parametrize("param", read_data_from_json(BASE_PATH + "/data/case.json"))
def test_case (param):
    print(f"uname={param['uname']}, pwd={param['pwd']}")