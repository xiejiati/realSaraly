__author__ = 'xjt'

import copy

path_stored = 'stored'
path_material = 'material'

#paths
pre_path_truck = names_pre_path = path_material

pre_path_personal_details_xsl = '\\personal_details'
pre_path__product_value_stored = '\\truck_details'
pre_path_sum_xsl = pre_path_other_fee = path_stored


postfix_other_fee = 'of'
file_name_other_fee = '话费'





money_per_liter = 7

#Commission of _product_value
single_commission = 0.1
double_commission = 0.09

#tel charge and social security
money_per_dayoff  = 17
tel_subside = 100

#alias of ui
date = '日期'
client = '客户'
product_value = '产值'
comment = '备注'
truck_weight = '车重'
oil = '加油'
miles = '公里'
drivers = '司机'
from_to = '起止'

header_item_in_order = []
header_item_in_order.append(date)
header_item_in_order.append(client)
header_item_in_order.append(product_value)
header_item_in_order.append(comment)
header_item_in_order.append(truck_weight)
header_item_in_order.append(oil)
header_item_in_order.append(miles)
header_item_in_order.append(drivers)
header_item_in_order.append(from_to)



#other terms
first_round = '第一趟'
second_round = '回头货'
first_record = '记录一'
second_record = '记录二'
personal = '个人'
cooperative = '两人'
light_truck = '空车'
first_level_heavy_truck = '重车'
second_level_heavy_truck = '超重车'
third_level_heavy_truck = '最重车'

#weight of car
oil_levels_weight_delimiter = {}
oil_levels_weight_delimiter[first_level_heavy_truck] = 25.5
oil_levels_weight_delimiter[second_level_heavy_truck] = 30.0



#coefficient
oil_per_mile_by_weight_coe = {}
oil_per_mile_by_weight_coe[light_truck] = 0.27
oil_per_mile_by_weight_coe[first_level_heavy_truck] = 0.4
oil_per_mile_by_weight_coe[second_level_heavy_truck] = 0.45
oil_per_mile_by_weight_coe[third_level_heavy_truck] = 0.5

#paths
file_name_trucks = '车牌'
file_name_drivers = '姓名'

#delimiter
driver_delimiter = ','
from_to_delimiter = '-'
stored_partition_delimiter = ':'

#empty slot difference between first record and second record
item_differences = 4
total_columns = 8
second_record_cols = 5

string_product_value = "产值（元）"
string_coe = '提成'
string_value = '值（元）'
string_total = '合计'
string_oil_single = '个人用油（升）'
string_oil_double = '两人用油/2（升）'
string_oil_subsidy_per_mile = '每公里补油（升）'
string_miles_single = '单人里程（公里）'
string_miles_double = '两人里程/2（公里）'
string_oil_subsidy = '应补油量（升）'
string_oil_own_single = '个人加油（升）'
string_oil_own_double = '两人加油/2（升）'
string_oil_saved = '省下的油（升）'
string_money_per_oil_liter = '每升油补（元/升）'
string_money_oil_saved = '油费补贴（元）'

#other fees
other_fee = []
other_fee_name = '姓名'
other_fee_days_off = '请假'
other_fee_phone_fee = '话费'
other_fee_deduction = '扣钱'
other_fee_comment = '备注'
other_fee.append(other_fee_name)
other_fee.append(other_fee_days_off)
other_fee.append(other_fee_phone_fee)
other_fee.append(other_fee_deduction)
other_fee.append(other_fee_comment)
other_fee_empty_fields = []
other_fee_empty_fields.append(other_fee_days_off)
other_fee_empty_fields.append(other_fee_phone_fee)
other_fee_empty_fields.append(other_fee_deduction)
string_other_fee_deduction_per_day = '每天扣钱（元）'
string_other_fee_days_off_deduction = '请假扣钱（元）'
string_other_fee_actual_phone_fee = '实际话费（元）'
string_other_fee_phone_fee_deduction = '话费应扣（元）'
string_other_fee_deduction = '扣款（元）'
string_other_fee_comment = '扣款事项'

string_personal_detail = '个人明细'

string_sum_truck = '车号'
string_sum_driver = '司机'
string_sum_product_value = '产值'
string_sum_remaining_oil = '省/耗油'
string_sum_money_oil = '油款'
string_sum_commission = '工资提成'
string_sum_tie = '补胎费'
string_sum_tel_ss = '话费社保'
string_sum_deduction = '扣款'
string_sum_deduction_reason = '扣款原因'
string_sum_total = "实发工资"

string_sum_items = []
string_sum_items.append(string_sum_truck)
string_sum_items.append(string_sum_driver)
string_sum_items.append(string_sum_product_value)
string_sum_items.append(string_sum_remaining_oil)
string_sum_items.append(string_sum_money_oil)
string_sum_items.append(string_sum_commission)
string_sum_items.append(string_sum_tie)
string_sum_items.append(string_sum_tel_ss)
string_sum_items.append(string_sum_deduction)
string_sum_items.append(string_sum_deduction_reason)
string_sum_items.append(string_sum_total)


coe_tie = 0.01
coe_salary = 0.09

string_salary_table = '工资表'
string_salary_sheet = '工资条'

xls_alignment = 'align: wrap on, horiz center'

def update_path(in_year_month):
    global pre_path_personal_details_xsl, pre_path__product_value_stored, pre_path_sum_xsl, pre_path_other_fee
    pre_path_personal_details_xsl = path_stored+'\\'+in_year_month+pre_path_personal_details_xsl
    pre_path__product_value_stored = path_stored+'\\'+in_year_month+pre_path__product_value_stored
    pre_path_other_fee = pre_path_sum_xsl = path_stored+'\\'+in_year_month




