#coding:UTF-8
__author__ = 'xiejiati'

import sys
sys.path.append(r'C:\Users\qing\PycharmProjects\untitled\Saraly')

from Saraly import *

stored_path = r'C:\Users\qing\Desktop\boy\粤k302.txt'

class translator:
    def stored_2_view(self):
        pass
    def stored_2_handler(self):
        lines = Model().read(stored_path)
        truck_name = stored_path.split('\\')[-1].split('.')[0]
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
                data2['客户'] = cols[1]
                data2['产值'] = cols[2]
                data2['备注'] = cols[3]
                data3 = {}
                data3['车重'] = cols[4]
                data3['加油'] = cols[5]
                data3['空车'] = cols[6]
                data3['重车'] = cols[7]
                data3['司机'] = cols[8].split(',')
                data3['起止'] = cols[9].split('-')
                data2['第一条记录'] = data3
                isSecondRound = lastData == cols[0]
                if isSecondRound:
                    data[cols[0]]['回头货'] = data2
                else:
                    data1 ={}
                    data1['第一趟'] = data2
                    data[cols[0]] = data1

                lastData = cols[0]
            else:
                data3 = {}
                data3['车重'] = cols[0]
                data3['加油'] = cols[1]
                data3['空车'] = cols[2]
                data3['重车'] = cols[3]
                data3['司机'] = cols[4].split(',')
                data3['起止'] = cols[5].split('-')
                if isSecondRound:
                    data[lastData]['回头货']['第二条记录'] = data3
                else:
                    data[lastData]['第一趟']['第二条记录'] = data3
        return truck_name, data

    def view_2_handler(self):
        pass
    def view_2_stored(self):
        pass

print(translator().stored_2_handler())
