# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/12/21 11:38
@File   ：house_service
@IDE    ：PyCharm
=================================================="""
"""
业务层，提供对房屋操作方法
"""

from house import *

class HouseService:

    # 定义属性houses列表，存放房屋对象
    houses = []

    # 定义属性id_counter，记录，当前房屋id
    id_counter = 1

    def __init__(self):
        # 为测试方便，在房屋列表中增加一个测试信息
        house = House(1,"tim","118","海淀",800, "未出租")
        self.houses.append(house)

    def get_houses(self):
        """
        返回房屋列表
        :return:
        """
        return self.houses

    def add_house(self, new_house:House):
        """
        将接收到的new_house 添加到houses列表中
        :param new_house:
        :return:
        """
        # 分配ID给new_house
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def find_by_id(self,find_id):
        """
        根据接收到的id 返回house对象
        :param find_id:
        :return:
        """
        for house in self.houses:
            if find_id == house.id:
                return house
        return None

    def del_by_id(self, del_id):
        """
        根据接收到的id删除房屋信息
        :param del_id:
        :return: 傻女胡成功，返回true;否则，返回false
        """
        # 判断deli_id是否存在
        house = self.find_by_id(del_id)
        if house is None:
            return False

        self.houses.remove(house)
        return True



