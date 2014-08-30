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
    def org_product_value_write(self, path, data):
        file = xlwt.Workbook(encoding='utf-8')
        table = file.add_sheet('sheet1', cell_overwrite_ok=True)
        line1 = data[0]
        cols = len(line1)
        rows = len(data)
        for i in range(rows):
            for j in range(cols):
                content = data[i][j]
                table.write(i, j, content.strip())
        file.save(path)












