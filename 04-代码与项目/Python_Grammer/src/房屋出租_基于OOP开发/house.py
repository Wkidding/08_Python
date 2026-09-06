# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/12/14 21:40
@File   ：house
@IDE    ：PyCharm
=================================================="""
"""
数据层：House类，一个House对象表示一个房屋
"""

class House:

    def __init__(self, id, name, phone, address, rent,state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    # 重写__str__魔术方法，按照固定格式输出房屋信息
    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rent}\t\t{self.state}"




