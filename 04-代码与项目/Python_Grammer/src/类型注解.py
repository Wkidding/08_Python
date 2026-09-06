# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2024/6/22 20:01
@File   ：类型注解
@IDE    ：PyCharm
==================================================
"""
from typing import Union, List, Set, Tuple, Dict

# 转义字符
# \n -- 换行符
print('123\n345')
print('123',end='$$$')  # 此时不换行
print('456')

# \t -- 制表符
print('123\t345')

# %% -- 输出%字符
score=98
print(f'成绩为：{score}%')

# f{string}模式--精度控制：
# {整型变量:06d}  -- 整型占6位，不足用0补齐，d可以省略
# {浮点型:.3f}  -- 保留3位小数，四舍五入
age=18
height=1.89
weight=83.782
stu_id=12345678
print(f'成绩为：{score},年龄为{age},身高{height:.4f},体重{weight:.6f},学号为{stu_id:06d}')







"""
类型注解:
    1、变量的类型注解
        变量名: 数据类型 = 数值
        
        注：
        Python中类型注解仅仅起到提示作用，没有其他语言那么严格
        Python解释器不会根据类型注解对数值做验证和判断，无法对应上也不会导致错误

    2、函数的类型注解
        def 函数方法名(形参名1:类型，形参名2:类型) -> 返回值类型：
	        函数体
    3、UNION类型（需要导包使用）
        联合类型注解，在变量注解、函数（方法）形参和返回值注解中均可使用
        当数据类型不唯一时基本格式无法满足要求，此时便可使用Union类型。使用示例，Union[类型,类型]：
"""

"""
1、变量类型注解
"""
# 及变量类型注解
var_1:int=10
var_2:float=12.34
var_3:str="asdf"
var_4:bool=True

# 类对象类型注解
class Student:
    pass

stu:Student=Student()  # 类对象类型注解，表示stu的类型是Student

# 基础容器注解
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_set:set={1,2,3}
my_dict:dict={'abc':666}
my_str:str="abcdefg"

# 基础容器详细注解
my_list2: List[int]=[1,2,3]
my_tuple2: Tuple[str,int,bool]=('abc',2,True) # 在tuple使用详细注解时，需要把每个元素类型都标记出来
my_set2: Set[int]={1,2,3}
my_dict2: Dict[str,int]={'abc':666}

"""
2、函数的类型注解
"""
def fun1(name:str):
    for ele in name:
        print("ele: {}".format(ele))

fun1("sdfasdgsdgs")

def func02(a:int, b:int) -> int:
    return a+b

print(func02(2, 3))

"""
3、Union的类型注解
"""
print("="*60)
a: Union[int, str] = 100
my_list02 : List[Union[int, str]] = [100, 200, 30, "abcdefgh"]