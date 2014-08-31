#coding:utf-8
__author__ = 'xjt'

def xls_generate_line(container, *items):
    container.append(items)

a = []
xls_generate_line(a, '1', 2, 3)
print(a)
