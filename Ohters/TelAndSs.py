__author__ = 'qing'

from util import *

def compute(days_off, tel_charge):
    remaining = tel_charge - tel_charge - money_per_dayoff * days_off
    if remaining < -500:
        remaining = -500
    return  remaining
