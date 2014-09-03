#coding:UTF-8
__author__ = 'xiejiati'

from variables import *
import util
import functools

class ProductValueTranslator:
    def stored_2_handler(self, lines):
        line_cols = len(lines)
        line_num = 0
        data = {}
        lastDate = ''
        isSecondRound = False
        while line_num < line_cols:
            line_dict = util.split_one_line_stored(lines[line_num])
            line_item_cols = len(line_dict)
            line_num += 1
            if line_item_cols > second_record_cols:
                data2 = {}
                data3 = {}
                data2[client] = line_dict[client]
                data2[product_value] = line_dict[product_value]
                data2[comment] = line_dict.setdefault(comment, '')

                data3[truck_weight] = line_dict[truck_weight]
                data3[oil] = line_dict[oil]
                data3[miles] = line_dict[miles]
                data3[drivers] = line_dict[drivers].strip().split(driver_delimiter)
                data3[from_to] = line_dict[from_to].strip().split(from_to_delimiter)
                data2[first_record] = data3
                isSecondRound = lastDate == line_dict[date]
                if isSecondRound:
                    data[line_dict[date]][second_round] = data2
                else:
                    data1 ={}
                    data1[first_round] = data2
                    data[line_dict[date]] = data1

                lastDate = line_dict[date]
            else:
                data3 = {}
                data3[truck_weight] = line_dict[truck_weight]
                data3[oil] = line_dict[oil]
                data3[miles] = line_dict[miles]
                data3[drivers] = line_dict[drivers].strip().split(driver_delimiter)
                data3[from_to] = line_dict[from_to].strip().split(from_to_delimiter)
                if isSecondRound:
                    data[lastDate][second_round][second_record] = data3
                else:
                    data[lastDate][first_round][second_record] = data3
        return data

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

class OtherFeeTranslator():
    def view_2_stored(self, data):
        out_data = []
        for data1 in data:
            out_data1 = '\t'.join(data1)+'\n'
            out_data.append(out_data1)
        return out_data

    def stored_2_view(self, data):
        out_data = []
        for data1 in data:
            items = data1.split()
            data2 = []
            for item in items:
                data2.append(item.partition(stored_partition_delimiter)[2])
            out_data.append(data2)
        return out_data

    def stored_2_handler(self, data):
        out_data = []
        for data1 in data:
            data1_dict = util.split_one_line_stored(data1)
            out_data.append(data1_dict)
        return out_data























