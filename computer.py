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
        return product_value

    def money_product_value(self, product_value):
        return self.money_product_value_single(product_value[personal])+ \
               self.money_product_value_double(product_value[cooperative])

    def money_product_value_single(self, value):
        return value*single_commission

    def money_product_value_double(self, value):
        return value*double_commission

    def miles(self, name, data):
        single = heavy_dict_producer()
        double = heavy_dict_producer()
        iter(compute_miles, data, name, single, double)
        miles = {}
        miles[personal] = single
        miles[cooperative] = double
        return miles


    def oil(self, name, data):
        single, double = record_array_producer()
        iter(comput_oil, data, name, single, double)
        oil = {}
        oil[personal] = single[0]
        oil[cooperative] = double[0]
        return oil

    def oil_total_own(self, oil_dict):
        return oil_dict[personal] + oil_dict[cooperative]

    def oil_saved(self, oil_own, oil_subsidy):
        return oil_subsidy - oil_own

    def oil_n_miles(self, miles, oil_per_mile):
        return miles*oil_per_mile

    def miles_level_total(self, miles_dict, truck_level):
        return miles_dict[personal][truck_level]+ miles_dict[cooperative][truck_level]

    def oil_subsidy_total(self, miles_dict):
        return self.oil_n_miles(self.miles_level_total(miles_dict, light_truck), oil_per_mile_by_weight_coe[light_truck]) +\
                self.oil_n_miles(self.miles_level_total(miles_dict, first_level_heavy_truck), oil_per_mile_by_weight_coe[first_level_heavy_truck]) +\
                self.oil_n_miles(self.miles_level_total(miles_dict, second_level_heavy_truck), oil_per_mile_by_weight_coe[second_level_heavy_truck]) +\
                self.oil_n_miles(self.miles_level_total(miles_dict, third_level_heavy_truck), oil_per_mile_by_weight_coe[third_level_heavy_truck])

    def money_oil_saved(self, oil_saved):
        return oil_saved * money_per_liter


class OtherFee:
    def tel_ss_remaining(self, days_off, tel_charge):
        self._remaining = tel_charge - tel_charge - money_per_dayoff * days_off
        if self._remaining < -500:
            self._remaining = -500
        return  self._remaining
