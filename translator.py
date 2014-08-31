#coding:UTF-8
__author__ = 'xiejiati'

from variables import *
import util
import functools

class ProductValueTranslator:
    def stored_2_handler(self, lines):
        size = len(lines)
        lineNum = 0
        data = {}
        lastData = ''
        isSecondRound = False
        while lineNum < size:
            line_dict = util.split_one_line_stored(lines[lineNum])
            line = '\t'.join(line_dict.values())
            lineNum += 1
            cols = line.strip().split()
            if cols == '': continue
            if len(cols) > total_columns:
                data2 = {}
                data2[client] = cols[1]
                data2[product_value] = cols[2]
                data2[comment] = cols[3]
                data3 = {}
                data3[truck_weight] = cols[4]
                data3[oil] = cols[5]
                data3[miles] = cols[6]
                data3[drivers] = cols[7].split(driver_delimiter)
                data3[from_to] = cols[8].split(from_to_delimiter)
                data2[first_record] = data3
                isSecondRound = lastData == cols[0]
                if isSecondRound:
                    data[cols[0]][second_round] = data2
                else:
                    data1 ={}
                    data1[first_round] = data2
                    data[cols[0]] = data1

                lastData = cols[0]
            else:
                data3 = {}
                data3[truck_weight] = cols[0]
                data3[oil] = cols[1]
                data3[miles] = cols[2]
                data3[drivers] = cols[3].split(driver_delimiter)
                data3[from_to] = cols[4].split(from_to_delimiter)
                if isSecondRound:
                    data[lastData][second_round][second_record] = data3
                else:
                    data[lastData][first_round][second_record] = data3
        return data

    def view_2_handler(self):
        pass

    def view_2_stored(self, data):
        lines = []
        for data1 in data:
            line = ''
            for v in data1.items():
                line += str(v[0])+':'+str(v[1]) + '\t'
            lines.append(line+'\n')
        return lines

    def stored_2_view(self, data):
        output_data = []
        for line in data:
            output_data1 = util.split_one_line_stored(line)
            output_data.append(output_data1)
        return  output_data

    def stored_2_xls(self, input):
        output = []
        titles = util.record_line_keys(input[0])
        titles.sort(key=functools.cmp_to_key(util.header_item_sort_key))
        output.append(titles)
        size = len(input)
        i = 0
        while i < size:
            line_items = []
            if util.is_odd(i):
                for j in range(item_differences):
                    line_items.append('')
            items = util.record_line_key_values(input[i])
            for item in sorted(items, key=functools.cmp_to_key(util.header_item_sort_tuple)):
                line_items.append(item[1])
            output.append(line_items)
            i += 1
        return output


















