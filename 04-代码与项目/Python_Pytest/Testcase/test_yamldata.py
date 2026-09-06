# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/21 07:19
@File   ：test_25
@IDE    ：PyCharm
=================================================="""
"""
pytest 使用parameter参数化获取yaml文件数据进行测试
"""

import pytest
import yaml
import os

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_data_from_yaml (file_path):
    f = open(file_path, "r", encoding="utf-8")
    res = yaml.load(f, yaml.FullLoader)
    f.close()
    print(f"返回的参数：{res}")
    return res

@pytest.mark.parametrize("param", read_data_from_yaml(BASE_PATH + "/data/case.yaml"))
def test_case (param):
    print(f"uname={param['uname']}, pwd={param['pwd']}")