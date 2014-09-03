#coding:utf-8
__author__ = 'xjt'

import variables
import util

class ProdutionValueView:
    def read(self, ui):
        data = []
        table = ui.tableWidget
        rowCnt = table.rowCount()
        for i in range(rowCnt):
            data1 = {}
            colCnt = table.columnCount()
            valid_item_count = 0
            for j in range(colCnt):
                if util.if_need_not_record(i, j):
                    continue
                header = table.horizontalHeaderItem(j).text().strip()
                item_text = table.item(i, j).text().strip()
                if header == variables.truck_weight and  item_text == '':
                    data1[header] = str(0)
                elif item_text != '':
                    data1[header] = item_text
                else:
                    valid_item_count += 1
                    if valid_item_count >= colCnt-1:
                        return data
                    else:
                        continue
            if len(data1) > 0:
                data.append(data1)
        return data

    def write(self, data, ui):
         table = ui.tableWidget
         self.clear_table_text(ui)
         size = len(data)
         for i in range(size):
             colCnt = table.columnCount()
             for j in range(colCnt):
                if util.if_need_not_record(i, j):
                    continue
                table_item = table.item(i, j)
                if table_item:
                    key = table.horizontalHeaderItem(j).text().strip()
                    if data[i] and isinstance(data[i], dict) and data[i].get(key):
                        table_item.setText(data[i][key])

    def current_truck_name(self, ui):
        return ui.comboBox.itemText(self.truck_combox_index(ui)).strip()

    def truck_name(self, index, ui):
        return ui.comboBox.itemText(index).strip()

    def truck_combox_index(self, ui):
        return ui.comboBox.currentIndex()

    def table_widget_enabled(self, state, ui):
        return ui.tableWidget.enabled(state)

    def clear_table_text(self, ui):
        for i in range(ui.tableWidget.rowCount()):
            for j in range(ui.tableWidget.columnCount()):
                item = ui.tableWidget.item(i, j)
                if item:
                    item.setText('')

class OtherFeeView:
    def read(self, ui):
        table = ui.tableWidget
        rowCnt = table.rowCount()
        colCnt = table.columnCount()
        data =[]
        for i in range(rowCnt):
            data1 = []
            empty_field_cnt = 0
            for j in range(colCnt):
                item = table.item(i, j)
                assert(item)
                item_text = item.text().strip()
                header_text =  table.horizontalHeaderItem(j).text()
                if item_text == '':
                    empty_field_cnt += 1
                    if empty_field_cnt == colCnt:
                        return data

                if item_text == '' and header_text in variables.other_fee_empty_fields:
                    item_text = str(0)
                data1.append(header_text+':'+item_text)
            data.append(data1)

    def write(self, ui, data):
        table = ui.tableWidget
        rowCnt = len(data)
        colCnt = table.columnCount()
        for i in range(rowCnt):
            for j in range(colCnt):
                table.item(i, j).setText(data[i][j])
















