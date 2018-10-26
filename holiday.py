#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/25/2018 1:54 PM
# @Author  : Aries
# @Site    : 
# @File    : holiday.py
# @Software: PyCharm



print('中国')

# 自动查询节日 给定起始日期和结束日期，自动获取总共的节假日天数

import datetime
from dateutil import rrule, easter

try:
    set
except NameError:
    from sets import Set as set


# 复活节
def all_easter(start, end):
    easters = [easter.easter(y) for y in xrange(start.year, end.year + 1)]
    return [d for d in easters if start <= d <= end]


# 开始到结束的节礼日列表
def all_boxing(start, end):
    one_day = datetime.timedelta(days=1)
    boxings = [easter.easter(y) + one_day for y in xrange(start.year, end.year + 1)]
    return [d for d in boxings if start <= d <= end]


# 返回开始和结束日期之间的圣诞节列表
def all_christmas(start, end):
    christmases = [datetime.date(y, 12, 25) for y in xrange(start.year, end.year + 1)]
    return [d for d in christmases if start <= d <= end]


# 返回劳动节列表
def all_labor(start, end):
    labors = rrule.rrule(rrule.YEARLY, bymonth=9, byweekday=rrule.MO(1), dtstart=start, until=end)
    return [d.date() for d in labors]


# 读取设定的节假日
def read_holidays(start, end, holidays_file='holidays.txt'):
    try:
        holidays_file = open(holidays_file)
    except IOError as err:
        print('open failed')
        return []

    holidays = []

    for line in holidays_file:
        if line.isspace() or line.startswith('#'):
            continue
        try:
            y, m, d = [int(x.strip()) for x in line.split(',')]
            date = datetime.date(y, m, d)
        except ValueError:
            print('Invalid line find')
            continue
        if start <= date <= end:
            holidays.append(date)
    holidays_file.close()
    return holidays


holidays_by_country = {
    'US': (all_easter, all_christmas, all_labor),
    'IT': (all_easter, all_boxing, all_labor)
}


def holidays(cc, start, end, holidays_file='holidays.txt'):
    all_holidays = read_holidays(start, end, holidays_file)
    functions = holidays_by_country.get(cc, ())
    for function in functions:
        all_holidays += function(start, end)
    all_holidays = list(set(all_holidays))
    return (len(all_holidays), all_holidays)


test_file = open(r'D:\123.txt', 'w')
test_file.write('2014,3,23')
test_file.close()

print(holidays('US', datetime.date(2016, 1, 1), datetime.date(2016, 12, 31), r'D:\123.txt'))
