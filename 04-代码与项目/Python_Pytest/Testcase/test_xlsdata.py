# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/7/22 06:29
@File   ：test_xlsdata
@IDE    ：PyCharm
=================================================="""
"""
pytest 使用parameter参数化获取excel文件数据进行测试
"""

import xlrd
import pytest
import os
import openpyxl

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def read_data_from_excel (file_path, sheet_name="Sheet1"):
#     # 打开文件
#     workbook = xlrd.open_workbook(file_path)
#
#     # 获取所有sheet
#     # sheets = workbook.sheet_names()
#     # print(sheets) # ['Sheet1', 'Sheet2', 'Sheet3']
#
#     # 根据sheet名称获取sheet内容(也可以格局索引，从0开始)
#     sheet = workbook.sheet_by_name(sheet_name)
#
#     # 获取第一行作为key
#     first_row = sheet.row_values(0)
#
#     # 获取行数
#     rows_length = sheet.nrows
#
#     all_rows = []
#     rows_dict = []
#
#     # 获取excel行数据
#     for i in range(rows_length):
#         if i < 1:
#             continue
#         all_rows.append(sheet.row_values(i))
#
#     # 遍历行数据列表，生成字典
#     for row in all_rows:
#         # print('=========',type(row))  # row是list类型
#
#         # zip()函数用于将可迭代的对象作为参数，将对象中对应的元素（索引相同的元素）打包成一个个元组，然后返回由这些元组组成的列表
#         # 然后通过dict转换为字典
#         lis = dict(zip(first_row, row))
#         # 每行字典数据放到列表
#         rows_dict.append(lis)
#     return rows_dict



def read_data_from_excel (file_path, sheet_name="Sheet1"):
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheet = wb[sheet_name]

    # 获取第一行作为键（取实际值，跳过空单元格）
    headers = [cell.value for cell in sheet[1] if cell.value is not None]

    rows_dict = []
    # 从第二行开始读取
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # 只取有数据的列（与headers长度一致）
        row_data = [cell for cell in row[:len(headers)] if cell is not None]
        if not row_data:  # 跳过全空行
            continue
        # 补齐长度（若某列值为None，用空字符串代替）
        while len(row_data) < len(headers):
            row_data.append('')
        rows_dict.append(dict(zip(headers, row_data)))
    return rows_dict

@pytest.mark.parametrize("param", read_data_from_excel(BASE_PATH + "/data/case.xlsx"))
def test_case (param):
    print(param)
    print(f"uname={param['uname']}, pwd={param['pwd']}")