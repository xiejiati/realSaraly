#coding:utf-8
__author__ = 'xjt'

import variables
import model
import translator
import xlwt

def compute_product_value(name, v, round, single, double):
    compute_product_each_record(name, v, round, single, double, variables.first_record)
    compute_product_each_record(name, v, round, single, double, variables.second_record)


def compute_product_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][variables.drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += float(v[round][variables.product_value])/2
        elif nDriver == 2:
            double[0] += float(v[round][variables.product_value])/4

def compute_miles(name, v, round, single, double):
    compute_miles_each_record(name, v, round, single, double, variables.first_record)
    compute_miles_each_record(name, v, round, single, double, variables.second_record)

def miles_init(dict):
    dict[variables.light_truck] = 0.0
    dict[variables.first_level_heavy_truck] = 0.0
    dict[variables.second_level_heavy_truck] = 0.0
    dict[variables.third_level_heavy_truck] = 0.0

def compute_miles_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][variables.drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[weight_rules(float(v[round][record][variables.truck_weight]))] += float(v[round][record][variables.miles])
        elif nDriver == 2:
            double[weight_rules(float(v[round][record][variables.truck_weight]))] += float(v[round][record][variables.miles])/2

def weight_rules(weight):
    if weight == 0:
        return variables.light_truck
    if weight < variables.oil_levels_weight_delimiter[variables.first_level_heavy_truck]:
        return variables.first_level_heavy_truck
    if weight < variables.oil_levels_weight_delimiter[variables.second_level_heavy_truck]:
        return variables.second_level_heavy_truck
    return variables.third_level_heavy_truck

#compute _oil
def comput_oil(name, v, round, single, double):
    comput_oil_each_record(name, v, round, single, double, variables.first_record)
    comput_oil_each_record(name, v, round, single, double, variables.second_record)

def comput_oil_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][variables.drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += float(v[round][record][variables.oil])
        elif nDriver == 2:
            double[0] += float(v[round][record][variables.oil])/2


def heavy_dict_producer():
    dict = {}
    dict[variables.light_truck] = 0
    dict[variables.first_level_heavy_truck] = 0
    dict[variables.second_level_heavy_truck] = 0
    return dict

def record_array_producer():
    single = []
    single.append(0)
    double = []
    double.append(0)
    return single, double

def iter(fun, data, name, single, double):
    for v in data.values():
        fun(name, v, variables.first_round, single, double)
        if v.get(variables.second_round):
            fun(name, v, variables.second_round, single, double)

def oil_per_mile_by_weight(data):
    oil_per_mile_by_weight_util(data,variables.light_truck)
    oil_per_mile_by_weight_util(data,variables.first_level_heavy_truck)
    oil_per_mile_by_weight_util(data,variables.second_level_heavy_truck)

def oil_per_mile_by_weight_util(data, type):
    return data[type] * variables.oil_per_mile_by_weight_coe[type]

def join_path(*path):
    return path[0]+'\\'+path[1]+'.'+path[2]

def if_need_not_record(row, col):
        return is_odd(row) and col < variables.item_differences

def lines_vaild_data(lines):
    items = []
    for line in lines:
        item = line.strip()
        if item != '':
            items.append(item)
    return items

def get_truck_names():
    m = model.CommonFileModel()
    path = join_path(variables.pre_path_truck, variables.file_name_trucks, 'txt')
    lines = m.read(path)
    return lines_vaild_data(lines)

def truck_name_contains_driver(driver_name):
    truck_names = get_truck_names()
    if len(truck_names) < 1:
        return ''
    m = model.CommonFileModel()
    t = translator.ProductValueTranslator()
    for truck_name in truck_names:
        path = join_path(variables.pre_path__product_value_stored, truck_name, 'pv')
        lines = m.read(path)
        if not lines: continue
        lines_after_transform = t.stored_2_view(lines)
        for line in lines_after_transform:
            for (k, v) in line.items():
                if k != variables.drivers: continue
                driver_array = v.split(variables.driver_delimiter)
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
        item_parts = item.partition(variables.stored_partition_delimiter)
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
    return cmp_fun(e1, e2,variables.header_item_in_order)

def sum_sort_cmp(e1, e2):
    return cmp_fun(e1[0],e2[0], variables.string_sum_items)


def cmp_fun(e1, e2, sort_array):
    e1_index = -1
    e2_index = -1
    i = 0
    size = len(sort_array)
    while i < size:
        if e1 == sort_array[i]:
            e1_index = i
        if e2 == sort_array[i]:
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

def other_fee_record_by_name(lines, driver_name):
    for line in lines:
        if driver_name == line[variables.other_fee_name]:
            return line

def open_work_book(path, sheet_name):
        file = xlwt.Workbook(encoding='utf-8')
        style = xlwt.easyxf(variables.xls_alignment)
        table = file.add_sheet(sheet_name, cell_overwrite_ok=True)
        return file, table, style

def single_array_write(data, table, start_row, style, num_lines):
    i = 0
    while i < num_lines:
        data1 = data[i]
        size_data1 = len(data1)
        for j in range(size_data1):
            if str(data1[j]) == '' : continue
            table.write(start_row, j, data1[j], style)

        i += 1
        start_row += 1

















