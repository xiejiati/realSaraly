__author__ = 'xjt'

#paths
pre_path_production_value = 'production_value'
pre_path_truck = names_pre_path = 'material'
pre_path_xsl = 'stored\\personal_details'
pre_path__product_value_stored = 'stored'





money_per_liter = 7

#Commission of _product_value
single_commission = 0.1
double_commission = 0.09

#tel charge and social security
money_per_dayoff  = 17
tel_subside = 100

#path prefix
path_product_value_package = r'stored'

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

string_product_value = "产值（元）"
string_coe = '提成'
string_value = '值（元）'
string_total = '合计'
string_oil_single = '个人用油（升）'
string_oil_double = '两人用油（升）'
string_oil_subsidy_per_mile = '每公里补油（升）'
string_miles_single = '单人公里'
string_miles_double = '两人公里'
string_oil_subsidy = '应补油量（升）'
string_oil_own_single = '个人加油（升）'
string_oil_own_double = '两人加油/2（升）'
string_oil_saved = '省下的油（升）'
string_money_per_oil_liter = '每升油补（元/升）'
string_money_oil_saved = '油费补贴（元）'


