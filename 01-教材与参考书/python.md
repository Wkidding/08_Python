# Python 知识体系

## Python 基础
### 环境与工具
- 安装 Python（版本管理：pyenv）
- 包管理器 pip / conda
- IDE（PyCharm / VS Code / Jupyter）

### 语法基础
- 变量与数据类型
- 运算符
- 输入输出（print, input, f-string）

### 流程控制
- 条件判断（if/elif/else）
- 循环（for, while, break, continue）

### 数据结构
- 列表、元组
- 字典、集合
- 切片与推导式

### 函数
- 定义与调用
- 参数类型（位置/关键字/默认/可变）
- 作用域与闭包
- lambda 表达式

### 模块与包
- import 机制
- `__name__ == "__main__"`
- 包结构（`__init__.py`）

## 面向对象编程（OOP）
### 类与对象
### 属性与方法
- 实例属性/类属性
- 实例方法/类方法/静态方法

### 三大特性
- 封装（`_` / `__`）
- 继承（单继承、多继承、MRO）
- 多态

### 特殊方法
- `__str__`, `__repr__`, `__call__` 等

### 装饰器
- @property, @classmethod, 自定义

## 高级特性
### 迭代器与生成器
- yield

### 装饰器（进阶）
- 带参数、类装饰器、多层

### 上下文管理器
- with, `__enter__/__exit__`, contextlib

### 元类
- 基础概念

### 并发编程
- 多线程（threading）
- 多进程（multiprocessing）
- 异步编程（asyncio, await/async）

## 标准库常用模块
### 文件与路径
- os, pathlib, shutil

### 时间
- datetime, time

### 数据处理
- json, csv, re（正则）

### 数学与随机
- math, random

### 系统与调试
- sys, logging

### 数据容器
- collections（deque, Counter, defaultdict）

## 第三方库（生态）
### 数据分析
- numpy, pandas

### 可视化
- matplotlib, seaborn

### Web 开发
- django, flask, fastapi

### 爬虫
- requests, beautifulsoup4, scrapy

### 数据库
- sqlalchemy, psycopg2, pymongo

### 自动化
- selenium, playwright

### 测试
- unittest, pytest

### 人工智能
- tensorflow, pytorch, scikit-learn

## 开发与工程
### 虚拟环境
- venv / virtualenv / conda

### 依赖管理
- requirements.txt, poetry

### 代码规范
- PEP8, pylint, black

### 类型注解
- typing 模块

### 单元测试与 Mock
### 调试技巧
- pdb, breakpoint

### 性能分析
- cProfile, line_profiler

### 打包发布
- setuptools, wheel

## 进阶主题
### 内存管理与垃圾回收
### 描述符（Descriptor）
### 设计模式（Pythonic 实现）
### C 扩展
- ctypes, Cython

### 并发模型
- GIL 理解

### 网络编程
- socket

## 学习资源
### 官方文档
### 书籍
- 流畅的 Python
- Python 编程：从入门到实践

### 练习平台
- LeetCode, Codewars