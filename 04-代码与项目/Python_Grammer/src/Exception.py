# -*- coding: UTF-8 -*-
'''===============================================
@Author ：kidding
@Date   ：2024/6/3 22:30
@File   ：Exception
@IDE    ：PyCharm
=================================================='''

"""
===============================================异常========================================
基本语法：
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
    else:
        没有出现异常执行的代码
    finally:
        finally表示的是无论是否异常都要执行的代码
    
# 未发生错误try全部代码都会执行
# 未发生错误不会执行except中的代码
# 发生错误try中只会执行到报错行为止的代码
# 发生错误会执行except中的代码
"""
# 捕获特定异常
try:
    print(name) # 未定义变量，报错
except NameError as e:
    print('name变量名称未定义错误')


# 捕获多个异常
try:
    print(num)          # 未定义，报错
except (NameError, ZeroDivisionError) as e:
    print(f"出现了异常，异常信息->{e}")            # 打印 name 'num' is not defined


# 打印异常信息。 异常描述信息存贮在别名中，可以通过打印别名获取
try:
    print(num) # 未定义，报错
except (NameError, ZeroDivisionError) as e:
    print(f"出现了异常，异常信息->{e}") # 打印 name 'num' is not defined


# 异常else，表示的是如果没有异常要执行的代码。
try:
    print(num) # 未定义，报错
except (NameError, ZeroDivisionError) as e:
    print(f"出现了异常，异常信息->{e}") # 打印 name 'num' is not defined
else:
    print("无异常") # 有异常，不执行

try:
    print("正常") # 不报错
except (NameError, ZeroDivisionError) as e:
    print(f"出现了异常，异常信息->{e}") # 不执行
else:
    print("无异常") # 执行


# 异常finally
global f
try:
    f = open("C:/code/aaa.txt", "r")
except Exception as e:
    print(f"出现了异常，异常信息->{e}")
finally:
    print("执行finally") # 执行


# 让用户输入一个整数，不是整数就一直抛出异常
num = 0
while True:
    try:
        num = int(input(f"请输入一个整数："))
        break
    except Exception as e:
        print(f"出现了异常，异常信息->{e}")
    finally:
        print(f"你输入的整数是{num}")
