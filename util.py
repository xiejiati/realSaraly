#coding:utf-8
__author__ = 'xjt'

from variables import *

def compute_product_value(name, v, round, single, double):
    lstDriver = v[round][first_record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round][product_value])
        elif nDriver == 2:
            double[0] += int(v[round][product_value])



def compute_miles(name, v, round, single, double):
    compute_miles_each_record(name, v, round, single, double, first_record)
    compute_miles_each_record(name, v, round, single, double, second_record)

def compute_miles_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[weight_rules(int(v[round][record][truck_weight]))] += int(v[round][record][miles])
        elif nDriver == 2:
            double[weight_rules(int(v[round][record][truck_weight]))] += int(v[round][record][miles])

def weight_rules(weight):
    if weight == 0:
        return light_truck
    elif weight < heavy:
        return heavy_truck
    else:
        return too_heavy_truck

#compute _oil
def comput_oil(name, v, round, single, double):
    comput_oil_each_record(name, v, round, single, double, first_record)
    comput_oil_each_record(name, v, round, single, double, second_record)

def comput_oil_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record][drivers]
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round][record][oil])
        elif nDriver == 2:
            double[0] += int(v[round][record][oil])


def heavy_dict_producer():
    dict = {}
    dict[light_truck] = 0
    dict[heavy_truck] = 0
    dict[too_heavy_truck] = 0
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
    oil_per_mile_by_weight_util(data,heavy_truck)
    oil_per_mile_by_weight_util(data,too_heavy_truck)

def oil_per_mile_by_weight_util(data, type):
    return data[type] * oil_per_mile_by_weight_coe[type]

def join_path(*path):
    return path[0]+'\\'+path[1]+'.'+path[2]

def if_need_not_record(row, col):
        return row % 2 == 1 and col < 4





