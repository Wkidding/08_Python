# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/12/14 21:43
@File   ：house_view
@IDE    ：PyCharm
=================================================="""
"""
界面层：显示界面，接受用户输入，调用业务层方法
"""

from house_service import *
from utility import *

class HouseView:
    # 定义属性 house_operation,类型是HouseService
    house_operation = HouseService()

    def main_menu(self):
        """
        显示主菜单
        :return:
        """
        while True:
            print()
            print("房屋出租系统菜单".center(32, "="))
            print("\t\t\t1 新增房源")
            print("\t\t\t2 查找房屋")
            print("\t\t\t3 删除房屋信息")
            print("\t\t\t4 修改房屋信息")
            print("\t\t\t5 房屋列表")
            print("\t\t\t6 退出")

            key = input("请输入你的选择（1~6）： ")
            if key in ["1","2","3","4","5","6"]:
                if key == "1":
                    self.add_house()
                elif key =="2":
                    self.find_house()
                elif key =="3":
                    self.del_house()
                elif key =="4":
                    self.update_house()
                elif key =="5":
                    self.list_houses()
                elif key =="6":
                    key = self.exit_sys()
                    if key:
                        break

    def list_houses(self):
        """
        显示房屋信息
        :return:
        """
        print("房屋列表".center(60, "="))
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(已租/未租)")
        # 得到houses列表
        houses = self.house_operation.get_houses()

        # 遍历房屋列表
        for house in houses:
            print(house)
            # 换行
        print()
        print("房屋列表显示完毕".center(60, "="))

    def add_house(self):
        """
        显示添加房屋界面，接受用户输入，构建 House对象
        :return:
        """
        print("添加房屋".center(32, "="))
        name = input("姓名：")
        phone = input("电话：")
        address = input("地址：")
        rent = int(input("租金："))
        status = input("状态：")

        # 构建房屋对象
        new_house = House(0, name, phone, address, rent, status)
        # 将新对象添加至房屋列表
        self.house_operation.add_house(new_house)

        print("添加房屋成功".center(32, "="))

    def del_house(self):
        """
        删除房屋界面，接受用户输入
        :return:
        """
        print("删除房屋信息".center(32, "="))
        del_id = int(input("请输入需要删除的房屋编号（-1退出）："))
        if del_id == -1:
            print("放弃删除房屋".center(32, "="))
            return

        choice = Utility.read_confirm_select()

        if choice.lower() == 'y':
            # 调用house_service层的删除方法
            if self.house_operation.del_by_id(del_id):
                print("删除房屋信息成功".center(32, "="))
            else:
                print("房屋编号不存在，删除失败...".center(32, "="))
        else:
            print("放弃删除房屋".center(32, "="))

    def exit_sys(self):
        choice = Utility.read_confirm_select()

        if choice.lower() == 'y':
            return True
        else:
            return False

    def find_house(self):
        """
        根据id查找房屋信息
        :param:
        :return:
        """
        print("查找房屋信息".center(32, "="))
        find_id = int(input("请输入需要查找的房屋编号："))
        house = self.house_operation.find_by_id(find_id)
        if house:
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(已租/未租)")
            print(house)
        else:
            print("房屋编号不存在，查找失败...".center(32, "="))

    def update_house(self):
        """
        更新房屋信息
        :return:
        """
        update_id = int(input("请选择待修改的房屋编号（-1表示退出）："))
        if update_id == -1:
            print("已放弃修改信息".center(32, "="))
            return
        else:
            # 找对应的房屋信息
            house = self.house_operation.find_by_id(update_id)
            if not house:
                print("待修改房屋不存在，修改失败...".center(32, "="))
                return

            # 返回的house是对象，直接修改对象属性即可
            house.name = Utility.read_str(f"姓名({house.name}): ",house.name)
            house.phone = Utility.read_str(f"电话({house.phone}): ", house.phone)
            house.address = Utility.read_str(f"地址({house.address}): ", house.address)
            house.rent = int(Utility.read_str(f"租金({house.rent}): ", house.rent))
            house.state = Utility.read_str(f"状态({house.state}): ", house.state)

        print("修改房屋信息成功".center(32, "="))
