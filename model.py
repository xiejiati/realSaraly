#coding:utf-8
__author__ = 'qing'

import xlwt

class CommonFileModel:
    def read(self, stored_path):
        try:
            with open(stored_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                i = 0
                size = len(lines)
                while i < size:
                    if lines[i].strip() == '':
                        del lines[i]
                    i += 1

                return lines
        except:
            return None



    def write(self, lines, path):
        with open(path, 'w+', encoding='utf-8') as f:
            f.writelines(lines)

class XslModel():
    def write(self, path, data, sheet_name, if_add_empty_line=True):
        file = xlwt.Workbook(encoding='utf-8')
        style = xlwt.easyxf('align: wrap on')
        table = file.add_sheet(sheet_name, cell_overwrite_ok=True)
        size = len(data)
        cur_index = 0
        i = 0
        while cur_index < size:
            data1 = data[cur_index]
            data1_rows = len(data1)
            for data1_row in range(data1_rows):
                data2 = data1[data1_row]
                data2_cols = len(data2)
                for j in range(data2_cols):
                    if str(data2[j]) == '':  continue
                    table.write(i, j, data2[j], style)
                if if_add_empty_line:
                    i += 1

            cur_index += 1
            i += 1
        file.save(path)












