#coding:utf-8
__author__ = 'xjt'

#paths
production_value_pre_path = 'production_value'

def compute_product_value(name, v, round, single, double):
    lstDriver = v[round]['第一条记录']['司机']
    nDriver = len(lstDriver)
    if name in lstDriver:
        if nDriver == 1:
            single[0] += int(v[round]['产值'])
        elif nDriver == 2:
            double[0] += int(v[round]['产值'])
