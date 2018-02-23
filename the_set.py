#!/usr/bin/env python3
# ! -*- coding:utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])    # set
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集

a = 'abc'
b = a.replace('a', 'A')
print(a,b)  #
