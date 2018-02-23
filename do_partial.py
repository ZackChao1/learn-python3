#!/bin/env python3
# -*- coding:utf-8 -*-

import functools

# 偏函数，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print(int('12345'))
print(int('12345', base=8))


def int2(x, base=2):
    return int(x, base)


print(int2('1010101'))
int3 = functools.partial(int, base=2)  # kw = { 'base': 2 } ；int('10010', **kw)
print(int3('11111111'))
