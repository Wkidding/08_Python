# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/8 15:21
@File   ：modlue_01
@IDE    ：PyCharm
=================================================="""

# 2、导入限制
# 在模块文件中使用 __all__ = ["func01"] 可以控制在其他文件使用 util_module0000.modlue_01 模块中，仅使用[]中的功能
# 导入方式为 from util_module0000 import modlue_02 *
__all__ = ["func01"]

# 注意：如果使用 “import 模块” 方式，则__all__失效：

def func01():
    print("module_02.py ：func01")

def func02():
    print("module_02.py ：func02")


# 内部测试代码，可以使用 __name__ 避免在外部引用该模块时运行模块内部的测试代码
if __name__ == "__main__":
    func01()
    func02()
    print("module_02.py ： {}".format(__name__))