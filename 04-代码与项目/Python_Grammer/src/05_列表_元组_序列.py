# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/8/24 20:59
@File   ：05_列表_元组_序列
@IDE    ：PyCharm
=================================================="""

import copy
from collections import namedtuple

# ==================== 5.1 列表的定义与操作 ====================
print("\n--- 5.1 列表的定义与操作 ---")

# 创建列表
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]
chars = list("Python")
range_list = list(range(5))
print("空列表:", empty)
print("数字列表:", numbers)
print("混合列表:", mixed)
print("嵌套列表:", nested)
print("list('Python'):", chars)
print("list(range(5)):", range_list)

# 索引与切片
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("原始:", fruits)
print("fruits[0]:", fruits[0])
print("fruits[-1]:", fruits[-1])
print("fruits[1:4]:", fruits[1:4])
print("fruits[:3]:", fruits[:3])
print("fruits[::2]:", fruits[::2])

# 查找索引 (index)
mylist = ['aaa', 'bbb', 'ccc']
print("mylist:", mylist)
print("mylist.index('bbb'):", mylist.index('bbb'))  # 返回1
# 若元素不存在会抛出 ValueError，此处注释以避免中断
# print(mylist.index('hello'))

# 切片赋值
fruits = ["apple", "banana", "orange", "grape", "mango"]
fruits[1:3] = ["kiwi", "peach"]
print("切片赋值后:", fruits)

fruits[2:2] = ["blueberry"]
print("通过切片插入:", fruits)

fruits[1:3] = []
print("通过切片删除:", fruits)

# 拼接与重复
a = [1, 2, 3]
b = [4, 5, 6]
print("a+b:", a + b)
print("a*2:", a * 2)

# 添加元素 (append, extend, insert)
lst = [1, 2, 3]
lst.append(4)
print("append后:", lst)
lst.extend([5, 6])
print("extend后:", lst)
lst.insert(1, 10)
print("insert(1,10)后:", lst)

# append vs extend 区别
lst = [1, 2]
lst.append([3, 4])
print("append([3,4]):", lst)
lst = [1, 2]
lst.extend([3, 4])
print("extend([3,4]):", lst)

# 删除元素 (remove, pop, del, clear)
lst = [10, 20, 30, 20, 40]
lst.remove(20)
print("remove(20)后:", lst)
removed = lst.pop()
print("pop()删除:", removed, "列表变为:", lst)
removed2 = lst.pop(1)
print("pop(1)删除:", removed2, "列表变为:", lst)
del lst[0]
print("del lst[0]后:", lst)
lst.clear()
print("clear后:", lst)

# 统计元素个数 (len, count)
sample = ['bbb', 'ccc', 'bbb', 'aaa', 'bbb']
print("sample:", sample)
print("len(sample):", len(sample))
print("sample.count('bbb'):", sample.count('bbb'))

# 排序与反转
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print("sort()升序:", nums)
nums.sort(reverse=True)
print("sort(reverse=True)降序:", nums)

original = [3, 1, 2]
new_sorted = sorted(original)
print("sorted(original):", new_sorted, "原列表:", original)

words = ["python", "java", "c", "javascript"]
words.sort(key=len)
print("按长度排序:", words)

words.reverse()
print("reverse后:", words)

# 遍历列表（while 和 for）
print("--- 遍历列表（while） ---")
def list_while_func():
    mylist = ['ckdnfsnksng', 2894, 'bbb', 'ccc', 31.259, 'abc']
    index = 0
    while index < len(mylist):
        print(f"while 遍历: {mylist[index]}")
        index += 1
list_while_func()

print("--- 遍历列表（for） ---")
def list_for_func():
    mylist = ['ckdnfsnksng', 2894, 'bbb', 'ccc', 31.259, 'abc']
    for element in mylist:
        print(f"for 遍历: {element}")
list_for_func()

# 列表推导式
squares = [x**2 for x in range(10)]
print("平方数:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("偶数平方:", even_squares)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for row in matrix for num in row]
print("展开二维列表:", flatten)

coords = [(x, y) for x in range(3) for y in range(2)]
print("坐标对:", coords)

words = ["apple", "banana", "cherry"]
indexed = [(i, word) for i, word in enumerate(words)]
print("带索引的列表:", indexed)


# ==================== 5.2 元组的定义与特性 ====================
print("\n--- 5.2 元组的定义与特性 ---")

# 创建元组
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (42,)
print("t1:", t1, "类型:", type(t1))
print("t2:", t2)
print("单元素元组:", t3, "类型:", type(t3))
print("(42) 是整数:", type((42)))

t5 = 1, 2, 3
print(f"省略括号：{t5},类型是{type(t5)}")


t6=tuple((1,2,3))
print(f'tuple((1,2,3)):{t6},类型是：{type(t6)}')

t6=tuple([1,2,3])
print(f'tuple([1,2,3]):{t6},类型是：{type(t6)}')

# t6=tuple(1,2,3)
# print(f'tuple(1,2,3):{t6},类型是：{type(t6)}') ## TypeError

t7 = tuple("Python")
print("tuple('Python'):", t7)

# index
t7=('aa',453,'aa','efs',453,'vf',21.36,453,'shebg')
print(f'取元组t7中的元素453 在元组中第一次出现的下标位置：{t7.index(453)}')
# print(f'取元组t7中不包含的元素123的下标位置：{t7.index(123)}') # 不存在该元素，因此报错

# count
print(f'元组t7中的元素453 在该元组中出现了{t7.count(453)}次')

# len(元组)
print(f'元组t7中的元素总个数为：{len(t7)}')

# 不可变性
t = (1, 2, [3, 4])
print("原始元组:", t)
# t[0] = 10  # TypeError，注释掉
# t.append(5) # AttributeError，注释掉

# 元组元素不可增删改
t8 =('aa',453,[1,2,3,4,5,6,7,8])
print(f'元组t8中的元素为：{t8}')
# t8.[0]='bb' # 元组元素不可增删改,报错

t8[2][3] = 56     # 元组中的list元素可增删改
print(f'元组t8中的元素为：{t8}')
del t8[2][0]
print(f'元组t8中的元素为：{t8}')
t8[2].insert(3,789)
print(f'元组t8中的元素为：{t8}')
t8[2].append(99999)
print(f'元组t8中的元素为：{t8}')

# 遍历元组
def while_tuple_func():
    index = 0
    while index < len(t7):
        print(f'while循环 遍历元组t7，第{index}个元素为：{t7[index]}')
        index+=1

while_tuple_func()

def for_tuple_func():
    index = 0
    for element in t7:
        print(f'for循环 遍历元组t7，第{index}个元素为：{t7[index]}')
        index+=1

for_tuple_func()



# 元组拆包
coordinates = (10, 20)
x, y = coordinates
print("拆包:", x, y)

a, b = 5, 10
a, b = b, a
print("交换后: a=", a, ", b=", b)

first, *rest = (1, 2, 3, 4)
print("first:", first, "rest:", rest)

*start, last = (1, 2, 3, 4)
print("start:", start, "last:", last)

first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "middle:", middle, "last:", last)

_, b, _ = (1, 2, 3)
print("忽略值后 b =", b)

# 具名元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Point:", p)
print("p.x:", p.x, "p.y:", p.y)
print("p[0]:", p[0], "p[1]:", p[1])

x, y = p
print("拆包: x=", x, "y=", y)

print("_fields:", p._fields)
print("_asdict():", p._asdict())

p2 = p._replace(x=99)
print("替换后:", p2)

Person = namedtuple('Person', 'name age city')
alice = Person('Alice', 25, 'Beijing')
print(f"{alice.name} is {alice.age} years old, lives in {alice.city}")


# ==================== 5.3 序列的通用操作 ====================
print("\n--- 5.3 序列的通用操作 ---")

lst = [3, 1, 4, 1, 5]
tpl = (1, 2, 3, 2, 2)

print("len(lst):", len(lst))
print("max(lst):", max(lst))
print("min(lst):", min(lst))
print("sum(lst):", sum(lst))
print("4 in lst:", 4 in lst)
print("6 not in lst:", 6 not in lst)
print("tpl.count(2):", tpl.count(2))
print("tpl.index(2):", tpl.index(2))
print("tpl.index(2, 2):", tpl.index(2, 2))

s = "Hello"
print("s[1:4]:", s[1:4])


# ==================== 5.4 深拷贝与浅拷贝 ====================
print("\n--- 5.4 深拷贝与浅拷贝 ---")

# 浅拷贝
original = [1, 2, [3, 4]]
shallow = original.copy()
print("原列表:", original)
print("浅拷贝:", shallow)

shallow[0] = 100
print("修改浅拷贝不可变元素后:")
print("原列表:", original)
print("浅拷贝:", shallow)

shallow[2].append(5)
print("修改浅拷贝可变子对象后:")
print("原列表:", original)
print("浅拷贝:", shallow)

# 深拷贝
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
print("\n深拷贝测试:")
print("原列表:", original)
deep[2].append(5)
deep[0] = 100
print("修改深拷贝后:")
print("原列表:", original)
print("深拷贝:", deep)

# 自定义对象拷贝
class MyClass:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"MyClass({self.data})"

obj = MyClass([1, 2, 3])
shallow_copy = copy.copy(obj)
deep_copy = copy.deepcopy(obj)
print("\n自定义对象拷贝:")
print("obj.data is shallow_copy.data:", obj.data is shallow_copy.data)
print("obj.data is deep_copy.data:", obj.data is deep_copy.data)


# ==================== 综合练习 ====================
print("\n--- 综合练习1：统计单词频率 ---")

# 练习：统计文本中单词出现频率（使用列表和字典）
text = "apple banana apple orange banana apple"
# 1、先转变为list,方便后续的操作。
# split() 是字符串的方法，默认以空白字符（空格、换行、制表符等）作为分隔符，将字符串分割成一个个子串，并返回一个列表。
words = text.split()

# 2、使用列表推导式去重（保留顺序）
unique = []
[unique.append(w) for w in words if w not in unique]

# 3、统计频率,使用字典推导式 {键: 值 for 变量 in 可迭代对象}
freq = {w: words.count(w) for w in unique}
print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}

# 4、按频率降序排序
# sorted() 函数对这个视图进行排序，返回一个新的列表，列表中的元素是这些元组。
#freq.items() 返回一个视图对象，包含字典中的所有键值对，每个键值对都是一个元组，形如 (单词, 频数)。
# key=lambda x: x[1] 指定排序的依据：对于每个元组 x，取它的第二个元素（即频数）作为排序键。
# reverse=True 表示降序排列，频数高的排在前面。
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_freq)  # [('apple', 3), ('banana', 2), ('orange', 1)]

# 5、使用元组拆包打印
for word, count in sorted_freq:
    print(f"{word}: {count}次")

print("\n--- 综合练习2：从列表中取出偶数（while 与 for 对比） ---")
list_work = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list_for = []
for element in list_work:
    if element % 2 == 0:
        even_list_for.append(element)
print("for 循环取出偶数:", even_list_for)

even_list_while = []
index = 0
while index < len(list_work):
    element = list_work[index]
    if element % 2 == 0:
        even_list_while.append(element)
    index += 1
print("while 循环取出偶数:", even_list_while)
