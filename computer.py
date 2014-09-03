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

    def money_tie_in_product_value(self, product_value_total):
        return product_value_total * coe_tie

    def money_salary_in_product_value(self, product_value_total):
        return product_value_total * coe_salary

    def miles(self, name, data):
        single = heavy_dict_producer()
        double = heavy_dict_producer()
        miles_init(single)
        miles_init(double)
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


class OtherFeeComputer:
    def phone_fee_days_off_deduction(self, days_off_deduction, phone_fee_deduction):
        return phone_fee_deduction + days_off_deduction

    def deduction_days_off(self, days_off):
        days_off_deduction = -money_per_dayoff * days_off
        if days_off_deduction < -400:
            days_off_deduction = -400
        return days_off_deduction

    def deduction_phone_fee(self, actual_phone_fee):
        return 100 - actual_phone_fee

    def deduction_total(self, phone_days_off, other):
        return phone_days_off+other

def actual_salary(product_value, oil, phone_ss, deduction):
    return product_value+oil+phone_ss+deduction

