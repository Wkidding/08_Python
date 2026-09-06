# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/12/14 17:26
@File   ：my_tools
@IDE    ：PyCharm
=================================================="""
from pygments.lexer import default


def read_confirm_select():
    """
    确认用户输入的是Y/N，不区分大小写，如果用户输入的不是Y/N就反复输入
    :return:
    """
    print("请输入你的选择Y/N,请确认选择：",end="")
    while True:
        key = input()
        if key.lower() == 'y' or key.lower() == 'n':
            break
        else:
            print("输入错误，请重新输入：",end="")
    return key.lower()

def read_str(tip, default_val):
    """
    读取用户输入，如果用户没有输入，则返回默认值
    :param tip: 提示信息
    :param default_val: 默认信息
    :return: 返回新信息
    """
    # 如果直接回车，保留原值
    str = input(tip)
    if len(str) > 0:  # 如果用户输入的有内容，则更新对应的信息
        return str
    else:
        return default_val