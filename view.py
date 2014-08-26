#coding:utf-8
__author__ = 'xjt'

import handler

class ProdutionValueView:
    def __init__(self, ui):
        self.ui = ui
        
    def read(self):
        data = []
        table = self.ui.tableWidget
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

    def write(self, data):
         table = self.ui.tableWidget
         self.__clear_text__(table)
         size = len(data)
         for i in range(size):
             colCnt = table.columnCount()
             for j in range(colCnt):
                if self.__if_need_not_record__(i, j):
                    continue
                item = table.item(i, j)
                if item:
                    item.setText(data[i][table.horizontalHeaderItem(j).text().strip()])

    def current_truck_name(self):
        return self.ui.comboBox.itemText(self.truck_combox_index()).strip()

    def truck_name(self, index):
        return self.ui.comboBox.itemText(index).strip()

    def truck_combox_index(self):
        return self.ui.comboBox.currentIndex()

    def table_widget_enabled(self, state):
        return self.ui.tableWidget.enabled(state)

    def __clear_text__(self, table):
        table.clearContents()

    def __if_need_not_record__(self, i, j):
        return i % 2 == 1 and j < 4









