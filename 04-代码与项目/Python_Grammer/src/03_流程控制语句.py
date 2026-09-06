# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/8/23 17:17
@File   ：03_流程控制语句
@IDE    ：PyCharm
=================================================="""

import math
import random


# ==================== 3.1 顺序结构 ====================
print("\n--- 3.1 顺序结构 ---")

radius = 5.0
area = math.pi * radius ** 2
print(f"半径为 {radius} 的圆面积为：{area:.2f}")

# ==================== 3.2 选择结构 ====================
print("\n--- 3.2 选择结构 ---")

# if 语句
age = 18
if age >= 18:
    print("您已成年，可以进入。")

score = 85
if score >= 60:
    print("及格")
    print("继续加油")
print("程序结束")

# if-else
number = 7
if number % 2 == 0:
    print(f"{number} 是偶数")
else:
    print(f"{number} 是奇数")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print(f"成绩 {score} 分，等级为 {grade}")

# 非布尔条件测试
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("姓名不能为空")

items = [1, 2, 3]
if items:
    print(f"共有 {len(items)} 项")

# 条件表达式（三元运算符）
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)

a, b = 10, 20
max_value = a if a > b else b
print(max_value)

score = 75
result = "优秀" if score >= 90 else ("良好" if score >= 70 else "需努力")
print(result)

# ==================== 3.3 循环结构 ====================
print("\n--- 3.3 循环结构 ---")

# while 循环
sum_value = 0
i = 1
while i <= 100:
    sum_value += i
    i += 1
print(f"1 到 100 的和为：{sum_value}")

# 用户输入验证（交互式）
print("--- 密码验证（请输入 123456 以退出）---")
password = ""
while password != "123456":
    password = input("请输入密码：")
print("密码正确，欢迎！")

# for 循环遍历
print("--- for 循环遍历 ---")
for char in "Python":
    print(char, end=" ")
print()  # 换行

fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

colors = ("红", "绿", "蓝")
for color in colors:
    print(color)

user = {"name": "Alice", "age": 25, "city": "深圳"}
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key} → {value}")

for num in {3, 1, 4, 1, 5}:
    print(num, end=" ")
print()

# range() 函数
print("--- range() 函数 ---")
for i in range(5):
    print(i, end=" ")
print()
for i in range(2, 6):
    print(i, end=" ")
print()
for i in range(1, 10, 2):
    print(i, end=" ")
print()
for i in range(10, 0, -2):
    print(i, end=" ")
print()

r = range(3, 10, 2)
print(f"len(r) = {len(r)}")
print(f"r[0] = {r[0]}")
print(f"7 in r = {7 in r}")
print(f"list(range(5)) = {list(range(5))}")

# 循环嵌套 - 乘法表
print("--- 乘法表 ---")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()

# 遍历二维列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("--- 二维列表遍历 ---")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# 嵌套组合
colors = ["红", "蓝"]
sizes = ["大", "中", "小"]
print("--- 颜色与尺寸组合 ---")
for color in colors:
    for size in sizes:
        print(f"{color}{size}", end=" ")
print()

# break 语句
print("--- break 示例 ---")
numbers = [5, 3, 8, -2, 7, 1]
for num in numbers:
    if num < 0:
        print(f"找到第一个负数：{num}")
        break
    print(f"检查 {num}")

# continue 语句
print("--- continue 示例（奇数） ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

print("--- continue 示例（过滤空值） ---")
words = ["Python", "", "代码", None, "示例"]
for word in words:
    if not word:
        continue
    print(word, end=" ")
print()

# else 子句
print("--- else 子句（质数判断） ---")
num = 17
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} 不是质数，能被 {i} 整除")
        break
else:
    print(f"{num} 是质数")

print("--- else 子句（查找元素） ---")
target = 5
nums = [1, 3, 7, 9, 2]
for item in nums:
    if item == target:
        print(f"找到了 {target}")
        break
else:
    print(f"未找到 {target}")

# ==================== 3.4 pass 语句与占位 ====================
print("\n--- 3.4 pass 语句 ---")

def future_function():
    pass

class FutureClass:
    pass

age = 25
if age >= 18:
    pass          # TODO: 实现成年逻辑
else:
    pass          # TODO: 实现未成年逻辑

try:
    result = 10 / 0
except ZeroDivisionError:
    pass          # 忽略除零错误（谨慎使用）

for i in range(10):
    pass          # 暂时什么都不做

def another_function():
    ...           # 使用 ... 也可占位

print("pass 占位执行完成（无输出）")

# ==================== 综合练习：猜数字游戏 ====================
print("\n--- 综合练习：猜数字游戏 ---")
target = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("🎯 猜数字游戏（1-100），你有 7 次机会")

while attempts < max_attempts:
    try:
        guess = int(input("请输入你的猜测："))
    except ValueError:
        print("请输入有效的整数！")
        continue

    attempts += 1

    if guess < target:
        print("太小了，再大一点")
    elif guess > target:
        print("太大了，再小一点")
    else:
        print(f"🎉 恭喜！用了 {attempts} 次猜中数字 {target}")
        break
else:
    print(f"😢 机会用尽！正确数字是 {target}")
