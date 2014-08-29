#coding:UTF-8
__author__ = 'xiejiati'

from variables import *

class Translator:
    def stored_2_handler(self, lines):
        size = len(lines)
        lineNum = 0
        data = {}
        lastData = ''
        isSecondRound = False
        while lineNum < size:
            line = lines[lineNum]
            lineNum += 1
            cols = line.strip().split()
            if cols == '': continue
            if len(cols) > 8:
                data2 = {}
                data2[client] = cols[1]
                data2[product_value] = cols[2]
                data2[comment] = cols[3]
                data3 = {}
                data3[truck_weight] = cols[4]
                data3[oil] = cols[5]
                data3[miles] = cols[6]
                data3[drivers] = cols[7].split(',')
                data3[from_to] = cols[8].split('-')
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
                data3[drivers] = cols[3].split(',')
                data3[from_to] = cols[4].split('-')
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
            output_data1 = {}
            items = line.split()
            for item in items:
                item_parts = item.partition(':')
                output_data1[item_parts[0]] = item_parts[2]
            output_data.append(output_data1)
        return  output_data









