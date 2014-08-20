#coding:utf-8
__author__ = 'xiejiati'

from util import *
from translator import *

class handler:
    def product_each(self, name, data):
        product_value = {}
        single = []
        single.append(0)
        double = []
        double.append(0)
        for v in data.items():
            compute_product_value(name, v, '第一趟', single, double)
            if v.get('回头货'):
                compute_product_value(name, v, '回头货', single, double)
        product_value['个人'] = single[0]
        product_value['两人'] = double[0]
        return product_value

    def miles_each(self, name, data):
        single = heavy_dict()
        double = heavy_dict()
        for v in data.values():
            compute_miles(name, v, '第一趟', single, double)
            if v.get('回头货'):
                compute_miles(name, v, '回头货', single, double)
        miles = {}
        miles['个人'] = single
        miles['两人'] = double
        return miles

    def oil_each(self, name, data):









#print (translator().stored_2_handler()[1])
print (handler().miles_each('已', translator().stored_2_handler()[1]))













