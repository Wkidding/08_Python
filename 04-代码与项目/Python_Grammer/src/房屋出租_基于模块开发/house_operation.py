# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/18 08:37
@File   ：house_operation
@IDE    ：PyCharm
=================================================="""
from my_tools import *

"""
1、使用字典来储存房屋信息
2、一个字典对象对应一个房屋信息
3、多个字典/房屋信息，存放在list中
4、house_list= [{"id":1,"name":"tim","phone":"132","address":"beijing","rent""800,"status":"未出租"}，{},{}...]
"""

# 全局变量
house_list = [{"id":1,"name":"tim","phone":"132","address":"北京","rent":800,"status":"未出租"}]
id_counter = 1

def main_menu():
    """
    显示主菜单
    :return:
    """
    print()
    print("房屋出租系统菜单".center(32,"="))
    print("\t\t\t1 新增房源")
    print("\t\t\t2 查找房屋")
    print("\t\t\t3 删除房屋信息")
    print("\t\t\t4 修改房屋信息")
    print("\t\t\t5 房屋列表")
    print("\t\t\t6 退出")

def list_houses():
    """
    显示房屋列表
    :return:
    """
    print("房屋列表".center(60,"="))
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(已租/未租)")
    # 遍历房屋列表
    for house in house_list:
        # 取出house的value
        for value in house.values():
            print(value, end="\t\t")
        # 换行
        print()
    print("房屋列表显示完毕".center(60,"="))

def add_house():
    """
    添加房屋
    :return:
    """
    print("添加房屋".center(32,"="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("租金："))
    status = input("状态：")
    global id_counter
    id_counter += 1

    # 构建房屋信息对应字典，并加入到list中
    house = {"id":id_counter,"name":name,"phone":phone,"address":address,"rent":rent,"status":status}
    #添加至房屋列表
    house_list.append(house)
    print("添加房屋成功".center(32,"="))

def find_by_id(find_id):
    """
    根据输入的find_id返回对应的房屋信息（即字典），若没有返回None
    :param find_id:
    :return:
    """
    # 遍历house_list列表
    for house in house_list:
        if house["id"] == find_id:
            return house
    # 如果没有找到，返回None
    return None

def delete_house():
    """
    根据ID删除房屋信息
    :return:
    """
    print("删除房屋信息".center(32,"="))
    del_id = int(input("请输入需要删除的房屋编号（-1退出）："))
    if del_id == -1:
        print("放弃删除房屋".center(32,"="))
        return

    choice = read_confirm_select()

    if  choice.lower() == 'y':
        # 根据输入的id查找房屋是否存在
        house = find_by_id(del_id)
        if house:
            house_list.remove(house)
            print("删除房屋信息成功".center(32, "="))
        else:
            print("房屋编号不存在，删除失败...".center(32,"="))
    else:
        print("放弃删除房屋".center(32, "="))

def exit_sys():
    choice = read_confirm_select()

    if choice.lower() == 'y':
        return True
    else:
        return False

def find_house():
    """
    根据id查找房屋信息
    :param:
    :return:
    """
    print("查找房屋信息".center(32, "="))
    find_id = int(input("请输入需要查找的房屋编号："))
    house = find_by_id(find_id)
    if house:
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(已租/未租)")
        # 取出house的value
        for value in house.values():
            print(value, end="\t\t")
        # 换行
        print()
    else:
        print("房屋编号不存在，查找失败...".center(32, "="))

def update_info():
    """
    更新房屋信息
    :return:
    """
    update_id = int(input("请选择待修改的房屋编号（-1表示退出）："))
    if update_id == -1:
        print("已放弃修改信息".center(32,"="))
        return
    else:
        # 找对应的房屋信息
        house = find_by_id(update_id)
        if not house:
            print("待修改房屋不存在，修改失败...".center(32, "="))
            return

        house['name'] = read_str(f"姓名({house['name']}): ", house['name'])
        house['phone'] = read_str(f"电话({house['phone']}): ", house['phone'])
        house['address'] = read_str(f"地址({house['address']}): ", house['address'])
        house['rent'] = int(read_str(f"租金({house['rent']}): ", house['rent']))
        house['status'] = read_str(f"状态({house['status']}): ", house['status'])


    print("修改房屋信息成功".center(32,"="))