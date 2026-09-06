# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/8 15:21
@File   ：modlue_01
@IDE    ：PyCharm
=================================================="""

def func01():
    print("module_01.py ： func01")

def func02():
    print("module_01.py ： func02")


# 内部测试代码，可以使用 __name__ 避免在外部引用该模块时运行模块内部的测试代码
if __name__ == "__main__":
    func01()
    func02()
    print("module_01.py ： {}".format(__name__))