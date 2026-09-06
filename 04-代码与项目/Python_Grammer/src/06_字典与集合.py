# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/8/25 06:13
@File   ：06_字典与集合
@IDE    ：PyCharm
=================================================="""
import time

# ==================== 6.1 字典的定义与操作 ====================
print("\n--- 6.1 字典的定义与操作 ---")

# 创建字典
# 空字典
empty = {}
dict1 = dict()
print("空字典:", empty)
print(f'字典 dict1 内容是：{dict1},类型是{type(dict1)}')

# 使用花括号
person = {"name": "Alice", "age": 25, "city": "Beijing"}
print(f'字典 person 内容是：{person},类型是{type(person)}')

# 使用 dict() 构造函数
person2 = dict(name="Bob", age=30, city="Shanghai")
person3 = dict([("name", "Charlie"), ("age", 35)])
print(f'字典 person2 内容是：{person2},类型是{type(person2)}')
print(f'字典 person3 内容是：{person3},类型是{type(person3)}')

# 字典键可以是不可变类型
d = {1: "one", 2: "two", (1, 2): "tuple key"}  # 元组可作为键
# d = {[1,2]: "list"}  # TypeError: unhashable type 'list'
print("d:", d)

# 基本操作：增删改查
person = {"name": "Alice", "age": 25}
print("原始:", person)
print("person['name']:", person["name"])
# print(person["gender"])  # KeyError，注释掉

person["city"] = "Beijing"   # 新增
person["age"] = 26           # 修改
print("添加/修改后:", person)

del person["city"]
print("del后:", person)

age = person.pop("age")
print("pop('age')返回:", age, "字典变为:", person)

person = {"a": 1, "b": 2, "c": 3}
item = person.popitem()
print("popitem()返回:", item, "字典变为:", person)

person.clear()
print("clear后:", person)


# 字典可以通过Key值来取得对应的Value
dict4 = {
    "张三": {"语文": 110, "数学": 100},
    "李四": {"语文": 90, "数学": 20},
    '王五': {"语文": 101, "数学": 10},
    "赵六": {"语文": 88, "数学": 60}
}
print(f'打印王五的数学成绩：{dict4["王五"]["数学"]}')

# 遍历，字典不支持索引访问，因此仅能使用for遍历
def for_dict_func():
    for dname in dict4:
        print(f'遍历字典dict4 : key为：{dname},语文成绩为：{dict4[dname]["语文"]}\t数学成绩为：{dict4[dname]["数学"]}')
for_dict_func()


# keys / values / items
person = {"name": "Alice", "age": 25, "city": "Beijing"}
keys = person.keys()
values = person.values()
items = person.items()
print("通过 keys 方法 获取字典的全部Key:", list(keys))
print("通过 values 方法 获取字典的全部values:", list(values))
print("通过 items 方法 获取字典的全部items:", list(items))

# 视图动态反映变化
keys = person.keys()
person["gender"] = "female"
print("动态变化后的keys:", list(keys))

# get / setdefault / update
person = {"name": "Alice", "age": 25}
print("get('name'):", person.get("name"))
print("get('age'):", person.get("age"))
print("get('city'):", person.get("city"))
print("get('gender', '未知'):", person.get("gender", "未知"))

person.setdefault("city", "Beijing")
print("setdefault后:", person)
person.setdefault("age", 30)
print("setdefault('age',30)后:", person["age"])

person.update({"job": "Engineer", "age": 26})
print("update后:", person)
person.update([("salary", 8000), ("level", "senior")])
print("update列表后:", person)

# 遍历
person = {"name": "Alice", "age": 25, "city": "Beijing"}
print("遍历键:")
for key in person:
    print(key, person[key])

print("遍历键值对:")
for key, value in person.items():
    print(f"{key}: {value}")

print("遍历值:")
for value in person.values():
    print(value)


# ==================== 6.2 字典推导式 ====================
print("\n--- 6.2 字典推导式 ---")

squares = {x: x**2 for x in range(5)}
print("平方映射:", squares)

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("偶数平方映射:", even_squares)

original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("交换键值:", swapped)

keys = ["name", "age", "city"]
values = ["Alice", 25, "Beijing"]
person = {k: v for k, v in zip(keys, values)}
print("zip构建字典:", person)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sum = {f"row{i}": sum(row) for i, row in enumerate(matrix)}
print("行求和:", row_sum)


# ==================== 6.3 字典的底层实现（哈希表） ====================
print("\n--- 6.3 字典的底层实现（哈希表） ---")

print("hash('hello'):", hash("hello"))
print("hash((1,2)):", hash((1, 2)))

class MyClass:
    pass
obj = MyClass()
d = {obj: "value"}
print("自定义类实例作为键:", d)

# 以下代码会引发 TypeError，注释掉以保持脚本运行
# class Unhashable:
#     def __eq__(self, other):
#         return True
# u = Unhashable()
# d = {u: "test"}  # TypeError

# 性能对比（仅演示）
print("\n--- 字典与列表查找性能对比（少量数据演示）---")
small_dict = {i: i for i in range(100000)}
small_list = list(range(100000))

start = time.perf_counter()
_ = small_dict[99999]
dict_time = time.perf_counter() - start

start = time.perf_counter()
_ = small_list.index(99999)
list_time = time.perf_counter() - start

print(f"字典查找耗时: {dict_time:.6f}s")
print(f"列表查找耗时: {list_time:.6f}s")


"""
===============================字典练习=============================
"""
dict_work={
   "张三":
       {"部门":"科技部","工资":3000,"级别":1},
   "李四":
       {"部门":"市场部","工资":5000,"级别":2},
   "王五":
       {"部门":"市场部","工资":7000,"级别":3},
   "赵六":
       {"部门":"科技部","工资":4000,"级别":1},
   "陈七":
       {"部门":"市场部","工资":6000,"级别":2}}
for name in dict_work:
    if dict_work[name]["级别"] == 1:
       dict_work[name]["级别"] += 1
       dict_work[name]["工资"] += 1000
    print(name,dict_work[name])


# ==================== 6.4 集合的定义与操作 ====================
print("\n--- 6.4 集合的定义与操作 ---")

# 创建集合
empty = set()
fruits = {"apple", "banana", "orange"}
unique = set([1, 2, 2, 3, 3, 4])
chars = set("hello")
print("空集合:", empty)
print("fruits:", fruits)
print("去重集合:", unique)
print("字符集合:", chars)

# 基本操作
s = {1, 2, 3}
s.add(4)
print("add(4)后:", s)
s.discard(2)
print("discard(2)后:", s)
s.discard(10)   # 无影响
print("discard(10)后:", s)
s.remove(3)
print("remove(3)后:", s)
# s.remove(10)   # KeyError，注释掉

s = {1, 2, 3, 4}
popped = s.pop()
print("pop()弹出:", popped, "剩余:", s)

s.clear()
print("clear后:", s)

s = {1, 2, 3}
print("1 in s:", 1 in s)
print("4 not in s:", 4 not in s)
print("len(s):", len(s))

# 集合运算
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A:", A, "B:", B)
print("交集 (A & B):", A & B)
print("并集 (A | B):", A | B)
print("差集 (A - B):", A - B)
print("对称差 (A ^ B):", A ^ B)

C = {1, 2}
print("C <= A:", C <= A)
print("C.issubset(A):", C.issubset(A))
print("A >= C:", A >= C)
print("A.issuperset(C):", A.issuperset(C))

print("A.isdisjoint({5,6}):", A.isdisjoint({5,6}))  # True，A中没有5或6

# 集合推导式
squares_set = {x**2 for x in range(10)}
print("平方集合:", squares_set)

odd_squares = {x**2 for x in range(10) if x % 2 == 1}
print("奇数平方集合:", odd_squares)

text = "hello world"
unique_chars = {c for c in text if c != ' '}
print("非空格字符集合:", unique_chars)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = {num for row in matrix for num in row if num % 2 == 0}
print("矩阵偶数集合:", evens)

# 应用
words = ["apple", "banana", "apple", "orange", "banana"]
unique_words = list(set(words))
print("去重列表:", unique_words)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("共同元素:", common)


# ==================== 6.5 frozenset（不可变集合） ====================
print("\n--- 6.5 frozenset ---")

fs = frozenset([1, 2, 3, 3, 4])
fs_empty = frozenset()
print("frozenset:", fs)
print("空frozenset:", fs_empty)

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print("fs1:", fs1, "fs2:", fs2)
print("fs1 & fs2:", fs1 & fs2)
print("fs1 | fs2:", fs1 | fs2)
print("fs1 - fs2:", fs1 - fs2)
print("fs1 ^ fs2:", fs1 ^ fs2)
print("2 in fs1:", 2 in fs1)
print("len(fs1):", len(fs1))

# frozenset 可作为字典键
d = {frozenset({1, 2}): "value"}
print("frozenset作为键的字典:", d)


# ==================== 综合应用 ====================
print("\n--- 综合应用 ---")
text = "apple banana apple orange banana apple"
words = text.split()
word_count = {}
unique_words = set(words)

for word in unique_words:
    word_count[word] = words.count(word)

print("单词计数:", word_count)

# 使用 frozenset 作为缓存键（演示）
cache = {}
def expensive_function(a, b):
    key = frozenset([a, b])   # 注意：顺序不影响缓存，但可能逻辑不对，仅演示
    if key in cache:
        print("缓存命中")
        return cache[key]
    result = a ** b  # 模拟耗时计算
    cache[key] = result
    return result

print("expensive_function(2,10):", expensive_function(2, 10))
print("expensive_function(10,2):", expensive_function(10, 2))  # 缓存命中，但结果与2**10相同，因为顺序不影响，实际业务需注意
