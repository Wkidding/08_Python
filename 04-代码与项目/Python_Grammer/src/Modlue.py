# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/8 15:22
@File   ：Modlue
@IDE    ：PyCharm
=================================================="""

# 1、导入
# 使用这种导入方式，会导入模块中所有功能
from util_module import modlue_01 as m1

print("Out of the module01 :" )
m1.func01()


# 2、导入限制
# 在模块文件中使用 __all__ = ["func01"] 可以控制在其他文件使用util_module.modlue_01 模块中，仅使用[]中的功能
from util_module.modlue_02 import *
# 注意：如果使用 “import 模块” 方式，则__all__失效

print("Out of the module02 :" )
func01()
# func02() # 报错。在modlue_02中使用 __all__=['func01']限制了只能在modlue_02模块外使用func01函数，因此报错




