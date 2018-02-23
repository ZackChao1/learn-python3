#!/bin/env python3
# -*- coding:utf-8 -*-

# itertools 提供处理迭代功能的函数，返回的是Iterator
import itertools

natiaals = itertools.count(1)  # count()创建无限的iterator
for n in natiaals:
    print(n)

cs = itertools.cycle('ABC')  # cycle()把序列无限重复
for c in cs:
    print(c)

ns = itertools.repeat('A', 3)  # repeat()重复带次数的元素
for n in ns:
    print(n)

natials = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, natials)  # takewhile截取序列
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):  # chain() 串联iterator
    print(c)

for key, group in itertools.groupby('aaabbb,23sdf0ew'):  # groupby()返回(key, sub-iterator)
    print(list(key), list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# example
def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_N = itertools.takewhile(lambda x: x <= 2 * N - 1, odd)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    odd_4 = itertools.cycle([4, -4])
    result = []
    for i in odd_N:
        result.append(next(odd_4) / i)
    # step 4: 求和:
    return sum(result)
