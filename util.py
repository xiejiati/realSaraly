#coding:utf-8
__author__ = 'xjt'

from variables import *
import model
import translator

def compute_product_value(name, v, round, single, double):
    lstDriver = v[round][first_record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += float(v[round][product_value])
        elif nDriver == 2:
            double[0] += float(v[round][product_value])/2



def compute_miles(name, v, round, single, double):
    compute_miles_each_record(name, v, round, single, double, first_record)
    compute_miles_each_record(name, v, round, single, double, second_record)

def compute_miles_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[weight_rules(float(v[round][record][truck_weight]))] += float(v[round][record][miles])
        elif nDriver == 2:
            double[weight_rules(float(v[round][record][truck_weight]))] += float(v[round][record][miles])/2

def weight_rules(weight):
    if weight == 0:
        return light_truck
    if weight < oil_levels_weight_delimiter[first_level_heavy_truck]:
        return first_level_heavy_truck
    if weight < oil_levels_weight_delimiter[second_level_heavy_truck]:
        return second_level_heavy_truck
    return third_level_heavy_truck

#compute _oil
def comput_oil(name, v, round, single, double):
    comput_oil_each_record(name, v, round, single, double, first_record)
    comput_oil_each_record(name, v, round, single, double, second_record)

def comput_oil_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += float(v[round][record][oil])
        elif nDriver == 2:
            double[0] += float(v[round][record][oil])/2


def heavy_dict_producer():
    dict = {}
    dict[light_truck] = 0
    dict[first_level_heavy_truck] = 0
    dict[second_level_heavy_truck] = 0
    return dict

def record_array_producer():
    single = []
    single.append(0)
    double = []
    double.append(0)
    return single, double

def iter(fun, data, name, single, double):
    for v in data.values():
        fun(name, v, first_round, single, double)
        if v.get(second_round):
            fun(name, v, second_round, single, double)

def oil_per_mile_by_weight(data):
    oil_per_mile_by_weight_util(data,light_truck)
    oil_per_mile_by_weight_util(data,first_level_heavy_truck)
    oil_per_mile_by_weight_util(data,second_level_heavy_truck)

def oil_per_mile_by_weight_util(data, type):
    return data[type] * oil_per_mile_by_weight_coe[type]

def join_path(*path):
    return path[0]+'\\'+path[1]+'.'+path[2]

def if_need_not_record(row, col):
        return is_odd(row) and col < item_differences

def lines_vaild_data(lines):
    items = []
    for line in lines:
        item = line.strip()
        if item != '':
            items.append(item)
    return items

def get_truck_names():
    m = model.CommonFileModel()
    path = join_path(pre_path_truck, file_name_trucks, 'txt')
    lines = m.read(path)
    return lines_vaild_data(lines)

def truck_name_contains_driver(driver_name):
    truck_names = get_truck_names()
    if len(truck_names) < 1:
        return ''
    m = model.CommonFileModel()
    t = translator.ProductValueTranslator()
    for truck_name in truck_names:
        path = join_path(pre_path__product_value_stored, truck_name, 'pv')
        lines = m.read(path)
        if not lines: continue
        lines_after_transform = t.stored_2_view(lines)
        for line in lines_after_transform:
            for (k, v) in line.items():
                if k != drivers: continue
                driver_array = v.split(driver_delimiter)
                if driver_name in driver_array:
                    return truck_name
    return ''

def combine_path_read(model, path_pre, path_name, path_postfix):
    path = join_path(path_pre, path_name, path_postfix)
    lines = model.read(path)
    return lines

def split_one_line_stored(line):
    items = line.split()
    output = {}
    for item in items:
        item_parts = item.partition(stored_partition_delimiter)
        output[item_parts[0]] = item_parts[2]
    return output

def is_odd(num):
    return num % 2 == 1

def record_line_keys(line_data):
    line_dict = split_one_line_stored(line_data)
    return list(line_dict.keys())

def record_line_key_values(line_data):
    line_dict = split_one_line_stored(line_data)
    return list(line_dict.items())

def header_item_sort_key(e1, e2):
    e1_index = -1
    e2_index = -1
    i = 0
    size = len(header_item_in_order)
    while i < size:
        if e1 == header_item_in_order[i]:
            e1_index = i
        if e2 == header_item_in_order[i]:
            e2_index = i
        i += 1
    if e1_index < e2_index:
        return -1
    elif e1_index > e2_index:
        return 1
    return 0

def header_item_sort_tuple(e1, e2):
    return header_item_sort_key(e1[0], e2[0])

def truck_name_by_driver_name(driver_truck_dict, driver_name):
    truck_name = ''
    if driver_truck_dict.get(driver_name):
        truck_name = driver_truck_dict[driver_name]
    else:
        truck_name = truck_name_contains_driver(driver_name)
        if truck_name == '': return
        driver_truck_dict[driver_name] = truck_name
    return  truck_name

def xls_generate_line(container, *items):
    container.append(items)











