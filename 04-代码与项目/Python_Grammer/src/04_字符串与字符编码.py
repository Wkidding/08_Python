# -*- coding: UTF-8 -*-
"""
===============================================
@Author ：kidding (合并两个文档的作者信息)
@Date   ：2026/8/23 (合并日期)
@File   ：字符串操作全面总结
@IDE    ：PyCharm
================================================
"""

import re

# ==================== 1. 字符串的索引与切片 ====================
print("\n--- 1. 字符串的索引与切片 ---")

s = "Python"
print("正向索引:")
print(s[0])   # 'P'
print(s[1])   # 'y'
print(s[5])   # 'n'

print("负索引:")
print(s[-1])  # 'n'
print(s[-2])  # 'o'
print(s[-6])  # 'P'

# 切片
s = "Hello, World!"
print("基础切片:")
print(s[0:5])      # "Hello"
print(s[7:12])     # "World"
print(s[:5])       # "Hello"
print(s[7:])       # "World!"
print(s[:])        # "Hello, World!"

print("负索引切片:")
print(s[-6:-1])    # "World"
print(s[-6:])      # "World!"

print("步长切片:")
print(s[::2])      # "Hlo ol!"
print(s[1::2])     # "el,Wrd"
print(s[::-1])     # "!dlroW ,olleH"
print(s[10:5:-1])  # "!roW"

s = "Python"
print("边界超出自动截断:")
print(s[1:100])    # "ython"
print(s[-10:3])    # "Pyt"

# 取出字符串中的某个字符（下标索引）
str1 = "you are the whole world of me"
print(f'str1字符串为{str1}')
print(f'取出字符串中的某个字符，使用下标索引方法：{str1[5]}')

# ==================== 2. 字符串的常用方法 ====================
print("\n--- 2. 字符串的常用方法 ---")

# 2.1 split / join
s = "apple,banana,orange"
fruits = s.split(",")
print("split:", fruits)

s2 = "a b  c\td\n"
print("split默认:", s2.split())

s3 = "one,two,three,four"
print("split限制次数:", s3.split(",", 2))
print("rsplit:", s3.rsplit(",", 2))

words = ["Hello", "World", "Python"]
result = " ".join(words)
print("join:", result)

chars = ['P', 'y', 't', 'h', 'o', 'n']
print("join字符:", ''.join(chars))

# 2.2 replace
text = "Hello, world! Hello, Python!"
print("replace全部:", text.replace("Hello", "Hi"))
print("replace限制次数:", text.replace("Hello", "Hi", 1))

# 2.3 strip / lstrip / rstrip
s = "  \t Hello  \n"
print("strip:", repr(s.strip()))
print("lstrip:", repr(s.lstrip()))
print("rstrip:", repr(s.rstrip()))

s2 = "***Python***"
print("strip('*'):", s2.strip("*"))
print("lstrip('*'):", s2.lstrip("*"))
print("rstrip('*'):", s2.rstrip("*"))

s3 = "xyHello xyzWorld yxz"
print("strip('xyz'):", s3.strip("xyz"))

# 额外示例：规整操作（删除指定字符串）
str3 = '   12aaacccbbbcccddcccd21   '
print(f'删除左右两边空格之前，str3源串为：{str3}')
print(f'删除左右两边空格之后，str3串为：{str3.strip()}')     # 去除左右两边的空格和换行符
print(f'删除左边空格之后，str3串为：{str3.lstrip()}')     # 去除左边的空格和换行符
print(f'删除右边空格之后，str3串为：{str3.rstrip()}')     # 去除右边的空格和换行符

str4 = '123aaacccbbbcccddcccd321'
str4 = str4.strip('123')
print(f'删除左右两边的123字符串之后，str4串为：{str4}') # 去除前后的指定字符串

# 2.4 find / index / count
s = "Hello, World! Welcome to Python."
print("find 'World':", s.find("World"))
print("find 'Java':", s.find("Java"))
print("rfind 'o':", s.rfind("o"))
print("index 'World':", s.index("World"))
# print(s.index("Java"))  # ValueError，注释掉
print("count 'o':", s.count("o"))
print("count 'Python':", s.count("Python"))
print("count 'o' 0-15:", s.count("o", 0, 15))

# index 方法示例（从第二个文档）
str1 = "you are the whole world of me"
element = str1.index('of')
print(f'通过 index 方法取出字符串str1中的 of 字符串所在的下标：{element}')

# 统计某字符串出现次数（第二个文档）
num = str3.count('ccc')
print(f'ccc在str3中出现的次数为：{num}')

# 统计字符串长度
print(f'str3字符出的长度为：{len(str1)}')

# 2.5 大小写转换
s = "Hello, World!"
print("upper:", s.upper())
print("lower:", s.lower())
print("capitalize:", s.capitalize())
print("title:", s.title())
print("swapcase:", s.swapcase())
print("isupper:", s.isupper())
print("islower:", s.islower())
print("HELLO.isupper:", "HELLO".isupper())

# 2.6 判断开头结尾 / 类型
s = "hello123"
print("startswith 'hell':", s.startswith("hell"))
print("endswith '123':", s.endswith("123"))
print("endswith (456,123):", s.endswith(("456", "123")))
print("abc.isalpha:", "abc".isalpha())
print("123.isdigit:", "123".isdigit())
print("abc123.isalnum:", "abc123".isalnum())
print("  .isspace:", "  ".isspace())
print("Hello.istitle:", "Hello".istitle())

# ==================== 3. 字符串的格式化 ====================
print("\n--- 3. 字符串的格式化 ---")

# 3.1 f-string
name = "Alice"
age = 30
score = 95.678
print(f"姓名：{name}，年龄：{age}")
a, b = 5, 3
print(f"{a} + {b} = {a + b}")
print(f"分数：{score:.2f}")
print(f"百分比：{score/100:.1%}")
name = "Python"
print(f"{name:>10}")
print(f"{name:<10}")
print(f"{name:^10}")
print(f"{name:*^10}")
print(f"大写：{name.upper()}")
print(f"{{name}}")

# 3.2 format()
print("{} + {} = {}".format(5, 3, 8))
print("{0} + {1} = {2}，{0} - {1} = {3}".format(5, 3, 8, 2))
print("{name} is {age} years old".format(name="Bob", age=25))
print("{:.2f}".format(3.14159))
print("{:>10}".format("hello"))
print("{:*^10}".format("hi"))

# 3.3 % 格式化
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % 3.14159)

# ==================== 4. 字符编码 ====================
print("\n--- 4. 字符编码 ---")

# 4.1 ord / chr
print("ord('A'):", ord('A'))
print("chr(65):", chr(65))
print("ord('中'):", ord('中'))
print("chr(20013):", chr(20013))
print("ord('€'):", ord('€'))
print("hex(8364):", hex(8364))

print("遍历 'Python' 的码点:")
for ch in "Python":
    print(f"{ch}: {ord(ch)}", end="  ")
print()

# 4.2 encode / decode
s = "Python 编程"
b1 = s.encode('utf-8')
print("UTF-8 编码:", b1)
print("类型:", type(b1))

b2 = s.encode('gbk')
print("GBK 编码:", b2)

s1 = b1.decode('utf-8')
print("UTF-8 解码:", s1)
s2 = b2.decode('gbk')
print("GBK 解码:", s2)

# 解码容错
data = b'\xe7\xbc\x96'  # UTF-8 编码的 '编'
print("UTF-8 解码:", data.decode('utf-8'))
print("GBK 解码忽略错误:", data.decode('gbk', errors='ignore'))

# ==================== 5. 正则表达式（re模块）基础 ====================
print("\n--- 5. 正则表达式基础 ---")

text = "我的电话是 138-1234-5678，备用电话 010-87654321。"

# match (从开头匹配)
m = re.match(r"\d+", text)
print("re.match 结果:", m)  # None

# search
s = re.search(r"\d{3}-\d{4}-\d{4}", text)
if s:
    print("search 找到:", s.group())

# findall
phone_numbers = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print("findall 结果:", phone_numbers)

# compile
pattern = re.compile(r"\d{3,4}-\d{7,8}")
all_phones = pattern.findall(text)
print("compile findall:", all_phones)

# finditer
print("finditer 迭代:")
for match in pattern.finditer(text):
    print(f"找到：{match.group()}，位置：{match.span()}")

# sub
new_text = re.sub(r"\d{3,4}-\d{7,8}", "***", text)
print("sub 替换后:", new_text)

# split
splits = re.split(r"\d+", "a1b22c333d")
print("split 按数字分割:", splits)

# 分组捕获
date = "2026-08-23"
m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date)
if m:
    print("完整匹配:", m.group(0))
    print("第1组:", m.group(1))
    print("第2组:", m.group(2))
    print("第3组:", m.group(3))
    print("所有分组:", m.groups())

# 常用示例
# 邮箱验证
email = "user@example.com"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(email_pattern, email):
    print("邮箱格式有效")

# 提取数字（整数或小数）
s_price = "价格：100元，折扣：85折，运费：12.5元"
numbers = re.findall(r"\d+\.?\d*", s_price)
print("提取数字:", numbers)

# 替换多个空白为一个空格
text2 = "Hello    World!   Python."
clean = re.sub(r"\s+", " ", text2)
print("压缩空白:", clean)

# 判断是否包含中文
def has_chinese(text):
    return bool(re.search(r"[\u4e00-\u9fa5]", text))

print("'Python' 含中文?", has_chinese("Python"))
print("'Python编程' 含中文?", has_chinese("Python编程"))

# 综合示例：提取HTML标签内文本
html = "<div class='content'>Hello <strong>Python</strong></div>"
texts = re.findall(r">(.*?)<", html)
print("HTML标签内文本:", texts)
clean_html = re.sub(r"<[^>]+>", "", html)
print("去除标签后:", clean_html)

# ==================== 6. 综合案例 ====================
print("\n--- 6. 综合案例：字符串操作实战 ---")

work_str = "aaaa lmn aaa lmn bcdefg hijk lmn opq rst"
# 统计有多少个 lmn 字符串
num = work_str.count('lmn')
print(f'lmn字符串在源串work_str：{work_str} 中出现则次数为：{num}')

# 将字符串中的空格替换为‘#’
work_str2 = work_str.replace(' ', '#')
print(f'源串work_str：{work_str} ,替换后为：{work_str2}')

# 按照‘#’分割字符串，得到列表
work_str2_list = work_str2.split('#')
print(f'分割字符串后，列表为：{work_str2_list}')

# 统计人名
str_name = "tom jack mary nono smith will sdwe"
print(f'人名列表为：{str_name.split(" ")}')
print(f'人名数量为：{len(str_name.split(" "))}')
# 替换指定名字为”中国“
str_name_new = str_name.replace("will", "中国")
print(f'替换后列表为：{str_name_new}')

# 将所有英文名字首字母改为大写
str_name_upper = ""
str_name_new2 = str_name_new.split(" ")
for ele in str_name_new2:
    if ele.isalpha():
        ele = ele.capitalize()
        str_name_upper += ele + " "
str_name_upper = str_name_upper.strip(" ")
print(f'替换后列表为：{str_name_upper}')