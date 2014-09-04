#coding:utf-8
__author__ = 'qing'

import xlwt
import util

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
    def multi_array_write(self, path, data, sheet_name):
        file, table, style = util.open_work_book(path, sheet_name)
        size = len(data)
        cur_index = 0
        i = 0
        while cur_index < size:
            data1 = data[cur_index]
            num_line = len(data1)
            util.single_array_write(data1, table, i, style, num_line)
            i += num_line+1
            cur_index += 1
        file.save(path)

    def single_array_write(self, path, data, sheet_name):
        file, table, style = util.open_work_book(path, sheet_name)
        num_line = len(data)
        util.single_array_write(data, table, 0, style, num_line)
        file.save(path)

















