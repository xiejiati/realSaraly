#coding:utf-8
__author__ = 'xiejiati'

from util import *
from translator import *

class product_handler:
    def product_value(self, name, data):
        single, double = record_array_producer()
        iter(compute_product_value, data, name, single, double)
        product_value = {}
        product_value['个人'] = single[0]
        product_value['两人'] = double[0]
        self._product_value = product_value
        return self._product_value

    def money_product_value(self):
        self._money_product_value = self._product_value['个人']*single_commission + self._product_value['两人']*double_commission
        return self._money_product_value

    def miles(self, name, data):
        single = heavy_dict_producer()
        double = heavy_dict_producer()
        iter(compute_miles, data, name, single, double)
        miles = {}
        miles['个人'] = single
        miles['两人'] = double
        self._miles = miles
        return self._miles

    def oil(self, name, data):
        single, double = record_array_producer()
        iter(comput_oil, data, name, single, double)
        oil = {}
        oil['个人'] = single[0]
        oil['两人'] = double[0]
        self._oil = oil
        return self._oil

    def remaining_oil(self, name, data):
        miles = self._miles
        bonus = oil_per_mile_by_weight(miles['个人']) + oil_per_mile_by_weight(miles['两人'])/2
        self._remaining_oil = self._oil['个人']+self._oil['两人']/2 - bonus
        return self._remaining_oil

    def money_oil(self):
        self._money_oil = self._remaining_oil * money_per_liter
        return self._money_oil


class others_handler:
    def money_days_off(self):
        pass

class ProductionViewHandler:
    def




#print (translator().stored_2_handler()[1])
print (product_handler().oil('甲', translator().stored_2_handler()[1]))
print (product_handler().product_value('甲', translator().stored_2_handler()[1]))
print (product_handler().miles('已', translator().stored_2_handler()[1]))













