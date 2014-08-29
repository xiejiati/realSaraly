__author__ = 'xjt'

#paths
production_value_pre_path = 'production_value'
truck_pre_path = names_pre_path = 'material'



#weight of car
heavy = 33

#coefficient
oil_per_mile_by_weight_coe = {}
oil_per_mile_by_weight_coe['轻车'] = 4
oil_per_mile_by_weight_coe['重车'] = 5
oil_per_mile_by_weight_coe['超重车'] = 6

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



#other terms
first_round = '第一趟'
second_round = '回头货'
first_record = '记录一'
second_record = '记录二'
personal = '个人'
cooperative = '两人'
light_truck = '轻车'
heavy_truck = '重车'
too_heavy_truck = '超重车'

#paths
path_trucks = r'material\车牌.txt'
path_drivers = r'material\姓名.txt'

#delimiter
driver_delimiter = ','
from_to_delimiter = '-'
stored_partition_delimiter = ':'

#empty slot difference between first record and second record
item_differences = 4
