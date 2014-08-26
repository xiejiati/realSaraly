#coding:utf-8
__author__ = 'xjt'

from variables import *

def compute_product_value(name, v, round, single, double):
    lstDriver = v[round]['记录一']['司机']
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round]['产值'])
        elif nDriver == 2:
            double[0] += int(v[round]['产值'])



def compute_miles(name, v, round, single, double):
    compute_miles_each_record(name, v, round, single, double, '记录一')
    compute_miles_each_record(name, v, round, single, double, '记录二')

def compute_miles_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record]['司机']
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[weight_rules(int(v[round][record]['车重']))] += int(v[round][record]['公里'])
        elif nDriver == 2:
            double[weight_rules(int(v[round][record]['车重']))] += int(v[round][record]['公里'])

def weight_rules(weight):
    if weight == 0:
        return '轻车'
    elif weight < heavy:
        return '重车'
    else:
        return '超重车'

#compute _oil
def comput_oil(name, v, round, single, double):
    comput_oil_each_record(name, v, round, single, double, '记录一')
    comput_oil_each_record(name, v, round, single, double, '记录二')

def comput_oil_each_record(name, v, round, single, double, record):
    lstDriver = v[round][record]['司机']
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round][record]['加油'])
        elif nDriver == 2:
            double[0] += int(v[round][record]['加油'])


def heavy_dict_producer():
    dict = {}
    dict['轻车'] = 0
    dict['重车'] = 0
    dict['超重车'] = 0
    return dict

def record_array_producer():
    single = []
    single.append(0)
    double = []
    double.append(0)
    return single, double

def iter(fun, data, name, single, double):
    for v in data.values():
        fun(name, v, '第一趟', single, double)
        if v.get('回头货'):
            fun(name, v, '回头货', single, double)

def oil_per_mile_by_weight(data):
    oil_per_mile_by_weight_util(data,'轻车')
    oil_per_mile_by_weight_util(data,'重车')
    oil_per_mile_by_weight_util(data,'超重车')

def oil_per_mile_by_weight_util(data, type):
    return data[type] * oil_per_mile_by_weight_coe[type]

def join_path(*path):
    return path[0]+'\\'+path[1]+'.'+path[2]



