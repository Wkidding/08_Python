# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2024/6/2 22:13
@File   ：Function
@IDE    ：PyCharm
=================================================="""

"""
1、基本定义
"""
def add(x, y):
    return x + y
    print("end not print")     # 该行 在return后不再执行输出
res = add(10, 6)
print(res)    # 只输出 16


"""
2、如果函数没有使用return语句返回数据，函数返回值为None，其类型是：<class ‘NoneType’>
"""
def say():
    print("hello world")
mes = say()
print(f'mes为：{mes},其类型为：{type(mes)}')


"""
3、函数的嵌套调用
"""
def fun_1():
    fun_2()
    print("----fun_1-----")

def fun_2():
    fun_3()
    print("----fun_2-----")

def fun_3():
    print("----fun_3----")

fun_1()

"""
4、参数生命周期
"""
def test1():
    num1 = 100   # 局部变量
    print(num1)

test1()          # 输出 100
#print(num1)     # 报错 name 'num1' is not defined

num2 = 100      # 全局变量
def test2():
    print(num2)
test2()           # 输出 100
print(num2)       # 输出 100

# global关键字：一般情况下，在函数内无法修改全局变量的值，使用 global关键字可以在函数内部声明变量为全局变量, 如下所示
num3 = 100
def test3():
    global num3     # 声明num3为全局变量
    num3 = 200
    print(num3)
test3()             # 输出 200
print(num3)         # 输出 200


"""
5、多返回值
    (1)按照返回值的顺序，写对应顺序的多个变量接收即可
    (2)变量之间用逗号隔开
    (3)支持return不同类型的数据
"""
def test4():
    return 9,6,7
x,y,z = test4()
print(f'x = {x}, y = {y}, z = {z}')

def test5():
    return "aaa", True, 16
x, y, z = test5()
print(f"第一个值为{x},第二个值为{y},第三个值为{z}")

"""
6、多种传参方式
    (1)位置参数 : 调用函数时根据函数定义的参数位置来传递参，传递的参数和定义的参数的顺序及个数必须一致
    (2)关键字参数 : 函数调用时通过“键=值”形式传递参数
        可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
        函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
    (3)缺省参数 : 也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
        所有位置参数必须出现在默认参数前，包括函数定义和调用
        当调用函数时没有传递参数, 就会使用默认是用缺省参数对应的值
        函数调用时，如果为缺省参数传值则修改默认参数值, 否则使用这个默认值
    (4)不定长参数 : 也叫可变参数. 用于不确定调用的时候会传递多少个参数(不传参也可以)的场景
        (a) 位置传递
            以*号标记一个形式参数，以元组的形式接受参数
            传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型
        (b)关键字传递
            关键字不定长传递以**号标记一个形式参数，以字典的形式接受参数
            参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典
"""
# 位置参数
def test6_1(name, age, gender):
    print(f'名字是{name},年龄{age}岁,性别{gender}')
test6_1('aaa',18,'男')

# 关键字参数
def test6_2(name, age, gender):
    print(f'名字是{name},年龄{age}岁,性别{gender}')
test6_2(name = 'aaa',age = 18, gender = '男')     # 使用关键字并且位置一一对应传参
test6_2(gender = '女', name = 'bbb', age = 36)    # 使用关键字，位置随意，传参
test6_2('ccc', gender = '女', age = 26)     # 混合使用关键字和位置传参，位置需对应，关键字顺序随意

# 缺省参数
def test6_3(name, age, gender='男'):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")
test6_3('TOM', 20)            # 输出 您的名字是TOM,年龄是20,性别是男
test6_3('TOM', 20, '女')      # 输出 您的名字是TOM,年龄是20,性别是女


# 不定长参数 -- 位置传递
def test6_4_1(*args):
    print(args)
    print(f"args数据是{args}，类型是{type(args)}")
test6_4_1('TOM')                # 输出 ('TOM',)
test6_4_1('TOM', 20, '女')      # 输出 ('TOM', 20, '女')

# 不定长参数 -- 关键字传递
def test6_4_2(**kwargs):
    print(kwargs)
    print(f"kwargs数据是{kwargs}，类型是{type(kwargs)}")
    for kwargs_name in kwargs:
        print("参数名{0}，参数值{1}".format({kwargs_name},{kwargs[kwargs_name]}))
test6_4_2(name='TOM', age=20)   # 输出 {'name': 'TOM', 'age': 20}


"""
7、递归调用
"""
def test(n):
    if n>2:
        test(n-1)
    print("n = {}".format(n))
test(4)


def factorial(n):
    if n == 1:
        return  1
    else:
        return factorial(n-1)*n
print(factorial(4))

# 输出斐波那契数列中指定位置的数
def fnb(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fnb(n-1) + fnb(n-2)
print(fnb(7))  # 数列为： 1,1,2,3,5,8,13 ...


"""
8、函数作为参数传递
    函数本身也可以像普通变量一样作为参数传递使用.
    (1)函数名存放的是函数所在空间的地址
    (2)通过 '函数名()' 的形式可执行所存放空间中的代码(执行函数)
    (3)函数名可以像普通变量一样赋值，func1 = func2
    (4)函数本身也可以像普通变量一样作为参数传递使用
"""
# 函数名存放的是函数所在空间的地址
def test7_1():
    print("hello world~")
print(test7_1)

# 通过 '函数名()' 的形式可执行所存放空间中的代码(执行函数)
def test7_2():
    print("hello world~")
test7_2()

# 函数名可以像普通变量一样赋值，test7_3_2 = test7_3_1
def test7_3_1():
    print("hello world~")
test7_3_2 = test7_3_1
test7_3_2() # 打印 hello world~


# 函数本身也可以像普通变量一样作为参数传递使用
def test7_4_1(x, y):
    return x + y
def test7_4_2(add):
    result = test7_4_1(6, 3)
    print(f'函数test7_4_1类型为：{type(test7_4_1)}')
    print(result)

test7_4_2(test7_4_1) # 调用test7_4_2函数，直接传入test7_4_1函数名称，在test7_4_2内部会调用test7_4_1函数进行执行






## 函数作为参数例子
def get_max_value(num1, num2):
    max_value = num1 if num1 > num2 else num2
    return max_value

def f1(fun, num1, num2):
    return get_max_value(num1, num2)

def f2(fun,num1,num2):
    return num1+num2, get_max_value(num1, num2)

# 调用
print("f1函数结果：{}".format(f1(get_max_value, 3, 5)))

sum_num, max_num = f2(get_max_value,87,92)
print("f2函数结果：num1+num2 = {}, max_value={}".format(sum_num,max_num))





"""
9、lambda匿名函数 : 无名称的函数
    (1) def关键字，可以定义带有名称的函数 :       有名称的函数，可以基于名称重复使用。
    (2) lambda关键字，可以定义匿名函数（无名称） : 无名称的匿名函数，只可临时使用一次。
    (3)定义格式： 
        lambda 传入参数：函数体(一行代码)
             # lambda 是关键字，表示定义匿名函数
             # 传入参数表示匿名函数的形式参数，如：x, y 表示接收2个形式参数
             # 函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
"""
def test8_1(test7_4_1):
    result = test7_4_1(16, 13)
    print(result)

test8_1(lambda x, y: x + y)
"""
等效于
def test7_4_1(x, y):
    return x + y
def test8_1(add):
    result = test7_4_1(16, 13)
    print(result)
test8_1(add)
"""

def fun1(num1, num2):
    return num1+num2

def test8_2(fun1, num1, num2):
    return fun1(num1, num2)

addnum112 = test8_2(lambda num1, num2: num1 if num1 > num2 else num2, 12, 10)
print(addnum112)  # 输出：12
