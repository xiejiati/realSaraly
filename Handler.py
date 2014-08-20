#coding:utf-8
__author__ = 'xiejiati'

from util import *
from translator import *

class handler:
    def product_each(self, name, data):
        single, double = record_array_producer()
        iter(compute_product_value, data, name, single, double)
        product_value = {}
        product_value['个人'] = single[0]
        product_value['两人'] = double[0]
        return product_value

    def miles_each(self, name, data):
        single = heavy_dict_producer()
        double = heavy_dict_producer()
        iter(compute_miles, data, name, single, double)
        miles = {}
        miles['个人'] = single
        miles['两人'] = double
        return miles

    def oil_each(self, name, data):
        single, double = record_array_producer()
        iter(comput_oil, data, name, single, double)
        oil = {}
        oil['个人'] = single
        oil['两人'] = double
        return oil


#print (translator().stored_2_handler()[1])
print (handler().oil_each('甲', translator().stored_2_handler()[1]))
print (handler().product_each('甲', translator().stored_2_handler()[1]))
print (handler().miles_each('已', translator().stored_2_handler()[1]))













