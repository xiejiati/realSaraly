#coding:utf-8
__author__ = 'xjt'

from PySide.QtGui import *


class ProdutionView:
    def read(self, table):
        data = []
        rowCnt = table.rowCount()
        for i in range(rowCnt):
            data1 = {}
            colCnt = table.columnCount()
            valid_item_count = 0
            for j in range(colCnt):
                if self.__if_need_not_record__(i, j):
                    continue
                header = table.horizontalHeaderItem(j).text().strip()
                table_widget = table.item(i, j)
                if not table_widget:
                    valid_item_count += 1
                    if valid_item_count >= colCnt-1:
                        return data
                    else:
                        continue
                item_text = table_widget.text().strip()
                if header == '车重' and  item_text == '':
                    data1[header] = str(0)
                else:
                    data1[header] = item_text

            data.append(data1)
        return data

    def write(self, table, data):
         self.__clear_text__(table)
         size = len(data)
         for i in range(size):
             colCnt = table.columnCount()
             for j in range(colCnt):
                if self.__if_need_not_record__(i, j):
                    continue
                table.item(i, j).setText(data[i][table.horizontalHeaderItem(j).text().strip()])

    def __clear_text__(self, table):
        table.clearContents()

    def __if_need_not_record__(self, i, j):
        return i % 2 == 1 and j < 4









