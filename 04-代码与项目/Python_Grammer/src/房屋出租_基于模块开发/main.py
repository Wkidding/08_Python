# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/18 08:37
@File   ：main
@IDE    ：PyCharm
=================================================="""
"""
出租系统主程序
"""
from house_operation import *

def main():
    """
    主入口
    :return:
    """
    # 调用main_menu()函数，显示主菜单
    while True :
        main_menu()

        key = input("请输入你的选择（1~6）： ")
        if key in ["1","2","3","4","5","6"]:
            if key == "1":
                add_house()
            elif key =="2":
                find_house()
            elif key =="3":
                delete_house()
            elif key =="4":
                update_info()
            elif key =="5":
                list_houses()
            elif key =="6":
                key = exit_sys()
                if key:
                    break


if __name__ == "__main__":
    main()
    print("已经退出系统，欢迎下次使用...")