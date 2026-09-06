# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/8/23 16:45
@File   ：01_变量、数据类型与运算符
@IDE    ：PyCharm
=================================================="""

import keyword
import math
import cmath

# ==================== 2.1 标识符、关键字与命名规范 ====================
print("\n--- 2.1 标识符、关键字与命名规范 ---")

# 合法标识符
name = "Alice"
user_name = "Bob"
_name = "private"
user2 = "Charlie"
print("合法标识符示例:", name, user_name, _name, user2)

# 查看关键字
print("Python关键字:", keyword.kwlist)
print("'class' 是关键字?", keyword.iskeyword("class"))
print("'name' 是关键字?", keyword.iskeyword("name"))

# PEP 8 命名规范示例
user_age = 25
total_price = 99.99

def calculate_discount(price, rate):
    return price * rate

class CustomerAccount:
    pass

MAX_CONNECTIONS = 100
API_BASE_URL = "https://api.example.com"

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def _validate_amount(self, amount):
        return amount > 0

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"

print("PEP 8 命名示例执行完成（无输出）")


# ==================== 2.2 变量：赋值与动态类型机制 ====================
print("\n--- 2.2 变量：赋值与动态类型机制 ---")

x = 10
name = "Python"
print("变量赋值:", x, name)

# 动态类型
a = "hello"
print(f"a 的类型: {type(a)}")
a = 42
print(f"a 的类型: {type(a)}")
a = [1, 2, 3]
print(f"a 的类型: {type(a)}")

# 共享引用
a = "Python"
b = a
print(f"a 的内存地址: {id(a)}")
print(f"b 的内存地址: {id(b)} (与 a 相同)")
a = [1, 2, 3]
print(f"b 仍指向原字符串: {b}")


# ==================== 2.3 基本数据类型 ====================
print("\n--- 2.3 基本数据类型 ---")

# 整数
age = 25
year = 2026
huge_number = 10 ** 100
print("大整数 (10^100):", huge_number)
binary = 0b1010
octal = 0o12
hexadecimal = 0xA
print("不同进制:", binary, octal, hexadecimal)

# 浮点数
pi = 3.14159
e = 2.71828
scientific = 1.23e-4
inf = float('inf')
neg_inf = float('-inf')
nan = float('nan')
print("科学计数法:", scientific)
print("无穷大:", inf, math.isinf(inf))
print("NaN:", nan, math.isnan(nan))

# 浮点精度问题
result = 0.1 + 0.1 + 0.1
print("0.1+0.1+0.1 =", result)
print("等于0.3?", result == 0.3)

def almost_equal(a, b, tol=1e-9):
    return abs(a - b) < tol
print("安全比较结果:", almost_equal(0.1 + 0.1 + 0.1, 0.3))

# 复数
c1 = 3 + 4j
c2 = complex(2, -3)
print("复数 c1:", c1, "实部:", c1.real, "虚部:", c1.imag)
print("c1 + c2 =", c1 + c2)
print("c1 * c2 =", c1 * c2)
print("c1 的模长:", abs(c1))
print("sqrt(-1) =", cmath.sqrt(-1))

# 布尔型
is_valid = True
is_empty = False
print("布尔值运算: True + True =", True + True)
print("True * 10 =", True * 10)
print("False - 1 =", False - 1)
print("type(True):", type(True))
print("isinstance(True, int):", isinstance(True, int))


# ==================== 2.4 字符串（str） ====================
print("\n--- 2.4 字符串（str） ---")

# 引号
s1 = 'Hello, World!'
s2 = "Hello, World!"
s3 = '''这是
多行
字符串'''
s4 = """这也是
多行
字符串"""
quote1 = "He said, 'Hello'"
quote2 = 'She said, "Hi"'
print("单引号:", s1)
print("双引号:", s2)
print("三引号（第一行）:", s3.split('\n')[0])

# 转义与原始字符串
print("换行测试\nHello")
print("制表符\tWorld")
print("反斜杠: C:\\Users\\Name")
print('It\'s ok')
path = r'C:\Users\Name\Documents'
print("原始字符串路径:", path)
regex = r'\d+\.\d+'
print("原始字符串正则:", regex)

# f-string
name = "Alice"
age = 30
score = 95.678
print(f"My name is {name} and I am {age} years old.")
a, b = 5, 10
print(f"The sum of {a} and {b} is {a + b}")
print(f"Score: {score:.2f}")
print(f"Name: {name:>10}")
print(f"Name: {name:<10}")
print(f"Name: {name:^10}")
print(f"Uppercase: {name.upper()}")

# format()
print("My name is {} and I am {} years old.".format("Alice", 30))
print("My name is {0} and I am {1} years old. {0} likes Python.".format("Alice", 30))
print("My name is {name} and I am {age} years old.".format(name="Alice", age=30))
print("Pi is {:.2f}".format(3.14159))
print("{:>10}".format("test"))


# ==================== 2.5 类型转换 ====================
print("\n--- 2.5 类型转换 ---")

# 隐式转换
result = 10 + 3.14
print("10 + 3.14 =", result, type(result))
result = 10 + True
print("10 + True =", result, type(result))

# 显式转换
print("int('123') =", int("123"))
print("int(3.99) =", int(3.99))
print("int(True) =", int(True))
print("float('3.14') =", float("3.14"))
print("float(5) =", float(5))
print("str(123) =", str(123))
print("str(3.14) =", str(3.14))
print("bool(0) =", bool(0))
print("bool(1) =", bool(1))
print("bool('') =", bool(""))
print("bool('Python') =", bool("Python"))
print("bool([]) =", bool([]))
print("bool([1, 2]) =", bool([1, 2]))
# 以下会报错，注释掉
# int("abc")  # ValueError


# ==================== 2.6 运算符与表达式 ====================
print("\n--- 2.6 运算符与表达式 ---")

# 算术
a, b = 10, 3
print(f"算术: {a}+{b}={a+b}, {a}-{b}={a-b}, {a}*{b}={a*b}, {a}/{b}={a/b}, {a}//{b}={a//b}, {a}%{b}={a%b}, {a}**{b}={a**b}")
print("字符串运算: 'Hello' + ' ' + 'World' =", "Hello" + " " + "World")
print("'Ha' * 3 =", "Ha" * 3)

# 比较
x, y = 10, 20
print(f"比较: {x}=={y}? {x==y}, {x}!={y}? {x!=y}, {x}>{y}? {x>y}, {x}<{y}? {x<y}")
print(f"{x}>=10? {x>=10}, {x}<=5? {x<=5}")
print("'apple' < 'banana'?", "apple" < "banana")
print("'Apple' < 'apple'?", "Apple" < "apple")

# 逻辑
age = 25
has_license = True
print(f"age>=18 and has_license: {age>=18 and has_license}")
print(f"age>=18 and age<21: {age>=18 and age<21}")
print(f"age<18 or has_license: {age<18 or has_license}")
print(f"age<18 or age>30: {age<18 or age>30}")
print("not has_license:", not has_license)
print("not (age>30):", not (age > 30))

def risky_call():
    print("Function called!")
    return True
print("短路测试 (False and risky_call()):")
result = False and risky_call()  # risky_call 不会被调用
print("短路测试 (True or risky_call()):")
result = True or risky_call()

# 位运算
a, b = 60, 13
print(f"位运算: {a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"{a} ^ {b} = {a ^ b}")
print(f"~{a} = {~a}")
print(f"{a} << 2 = {a << 2}")
print(f"{a} >> 2 = {a >> 2}")

# 赋值
x = 10
x += 5
x *= 2
x //= 4
x %= 3
print("赋值运算后 x =", x)

# 身份
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")
print(f"a == c: {a == c}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a is not b: {a is not b}")
print(f"a is not c: {a is not c}")

x, y = 256, 256
print(f"256 is 256? {x is y}")   # 小整数缓存
x, y = 257, 257
print(f"257 is 257? {x is y}")   # 可能 False（取决于实现）

# 成员
print("'a' in 'apple':", 'a' in 'apple')
print("'z' in 'apple':", 'z' in 'apple')
print("'pp' in 'apple':", 'pp' in 'apple')
fruits = ['apple', 'banana', 'orange']
print("'banana' in fruits:", 'banana' in fruits)
print("'grape' in fruits:", 'grape' in fruits)
print("'grape' not in fruits:", 'grape' not in fruits)
user = {'name': 'Alice', 'age': 30}
print("'name' in user:", 'name' in user)
print("'Alice' in user:", 'Alice' in user)
print("'age' not in user:", 'age' not in user)


# ==================== 2.7 运算符优先级 ====================
print("\n--- 2.7 运算符优先级 ---")

result = 2 + 3 * 4
print("2 + 3 * 4 =", result)
result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)
result = 100 / 25 * 16
print("100 / 25 * 16 =", result)  # 左结合
result = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result)    # 右结合
a = b = c = 10
print("链式赋值: a, b, c =", a, b, c)

x, y, z = 5, 3, 2
result = x + y * z ** 2 > 20 and not x < y
print("复杂表达式结果:", result)
# 分解说明
print("分解: z**2=4, y*4=12, x+12=17, 17>20=False, x<y=False, not False=True, False and True = False")




# 2.8格式化输出

aa=12
bb=22.4
cc='中'
dd="python"

print("a= %d" % aa)
print("a= %f" %  bb)
print("a= %c" % cc)
print("a= %s" % dd)

## 使用 format函数进行格式化输出
print("aa={0},bb={1},cc={2},dd={3}".format(aa,bb,cc,dd))

## 使用 f-string进行输出
print(f"aa={aa},bb={bb},cc={cc},dd={dd}")


num1=30
num2=23
if (num1+num2)%3==0 and (num1+num2)%5==0:
    print(f"这个数字{num1+num2}可以被3、5整除")
else:
    print(f"这个数字{num1+num2}不能被3、5整除")


year=int(input("年份："))
if (year%4==0 and year%100!=0) or year %400==0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")



# range（）函数的区间为：前闭后开
for i in range(10):
    print("循环控制：{}".format(i)) # i循环为0~9


# 如果走到了break，则不走else;反之则会走到else
for i in range(5):
    print("遍历输出：{}".format(i))
    if i==20:
        break
else:
    print("循环结束,没有数据")



i = 0
j = 6
while j - i >= 0:
    print(f"{i} + {j-i} = {j}")
    i += 1


# 实心金字塔
for ii in range(6):
    print(" " * (5-ii), end="")
    for jj in range(2*ii - 1):
        print("*", end ="")
    print("")

# 空心金字塔
total_level=10
for ii in range(1, total_level + 1):
    print(" " * (total_level-ii), end="")
    for jj in range(2*ii - 1):
        if jj ==0 or jj == 2*ii-1-1 or ii == total_level:
            print("*", end ="")
        else:
            print(" ",end="")
    print("")


# 求3个班，每班5人，学生的平均分&每个班及格人数
total_class=3
total_num =5
total = 0
great_score = 0
for ii in range(0, total_class):
    print(f"请输入第{ii + 1}班各个学生的成绩：")
    for jj in range(0, total_num):
        num = float(input(f"第{jj+1}个学生的成绩："))
        total +=num
        if num>=60:
            great_score +=1
    print(f"{ii+1}班学生总成绩为{total}")
    print(f"{ii+1}班学生平均成绩为{total/total_num}")
    print(f"{ii+1}班学生及格人数为{great_score}")
    great_score=0
    print("")
