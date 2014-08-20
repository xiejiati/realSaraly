#coding:utf-8
__author__ = 'xjt'

#paths
production_value_pre_path = 'production_value'


#weight of car
heavy = 33

def compute_product_value(name, v, round, single, double):
    lstDriver = v[round]['记录一']['司机']
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round]['产值'])
        elif nDriver == 2:
            double[0] += int(v[round]['产值'])



def compute_miles(name, v, round, single, double):
    compute_miles_util(name, v, round, single, double, '记录一')
    compute_miles_util(name, v, round, single, double, '记录二')

def compute_miles_util(name, v, round, single, double, record):
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

def heavy_dict():
    dict = {}
    dict['轻车'] = 0
    dict['重车'] = 0
    dict['超重车'] = 0
    return dict


