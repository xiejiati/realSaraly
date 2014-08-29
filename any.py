#coding:utf-8
__author__ = 'xjt'

import xlrd

data = xlrd.open_workbook(r'material\\示例.xlsx')
table = data.sheet_by_index(0)
for i in range(table.nrows):
    print(table.row_values(i))
