# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2025/11/10 07:23
@File   ：abstract_method
@IDE    ：PyCharm
=================================================="""
from abc import ABC, abstractmethod

## 抽象类,继承ABC模块（需要导入）
class Animal(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 声明一个抽象方法
    @staticmethod
    def cry(self):
        # 作为抽象类让子类去实现该功能
        pass
# 抽象类（含有抽象方法），不能实例化

class Tiger(Animal):
    def cry(self):
        print("老虎{}嗷嗷叫".format(self.name))

tiger= Tiger("大老虎",2)
tiger.cry()


import time
class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    def cal_time(self):
        start = time.time()
        self.job()
        end = time.time()
        print("执行持续时间为：{}".format(end-start))

class AA(Template):
    def job(self):
        num = 0
        for i in range(1,100001):
            num +=i


class BB(Template):
    def job (self):
        num = 0
        for i in range(1,10001):
            num -=i

aa=AA()
aa.cal_time()
bb=BB()
bb.cal_time()