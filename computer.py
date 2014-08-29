__author__ = 'xjt'

from util import *
from variables import *

class ProductValueComputer:
    def product_value(self, name, data):
        single, double = record_array_producer()
        iter(compute_product_value, data, name, single, double)
        product_value = {}
        product_value[personal] = single[0]
        product_value[cooperative] = double[0]
        self._product_value = product_value
        return self._product_value

    def money_product_value(self):
        self._money_product_value = self._product_value[personal]*single_commission + self._product_value[cooperative]*double_commission
        return self._money_product_value

    def miles(self, name, data):
        single = heavy_dict_producer()
        double = heavy_dict_producer()
        iter(compute_miles, data, name, single, double)
        miles = {}
        miles[personal] = single
        miles[cooperative] = double
        self._miles = miles
        return self._miles

    def oil(self, name, data):
        single, double = record_array_producer()
        iter(comput_oil, data, name, single, double)
        oil = {}
        oil[personal] = single[0]
        oil[cooperative] = double[0]
        self._oil = oil
        return self._oil

    def remaining_oil(self, name, data):
        miles = self._miles
        bonus = oil_per_mile_by_weight(miles[personal]) + oil_per_mile_by_weight(miles[cooperative])/2
        self._remaining_oil = self._oil[personal]+self._oil[cooperative]/2 - bonus
        return self._remaining_oil

    def money_oil(self):
        self._money_oil = self._remaining_oil * money_per_liter
        return self._money_oil

class OtherFee:
    def tel_ss_remaining(self, days_off, tel_charge):
        self._remaining = tel_charge - tel_charge - money_per_dayoff * days_off
        if self._remaining < -500:
            self._remaining = -500
        return  self._remaining
