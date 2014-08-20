#coding:utf-8
__author__ = 'xiejiati'

from util import *
from translator import *

class handler:
    def product_each(self, name, data):
        product = {}
        single = []
        single.append(0)
        double = []
        double.append(0)
        for k, v in data.items():
            compute_product_value(name, v, '第一趟', single, double)
            if v.get('回头货'):
                compute_product_value(name, v, '回头货', single, double)
        product['个人'] = single[0]
        product['两人'] = double[0]
        return product

    def 

#print (translator().stored_2_handler()[1])
print (handler().product_each('甲', translator().stored_2_handler()[1]))













