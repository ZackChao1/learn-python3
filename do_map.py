#!/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce


def f(x):
    return x * x


# use map()将传入的函数依次作用到list的每个元素，返回一个iterator
r = map(f, [1, 2, 3, 4])  # r is Iterator
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# use reduce()将一个函数作用在list上，并把结果继续和序列的下一个元素做累积计算
def add(x, y):  # reduce()函数必接收两个参数
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 4, 5, 6]))


def char2num(s):  # str 转换为 Int
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))  # map() and reduce() with togther

# 规范名称
print(list(map(lambda name: name[0].upper() + name[1:].lower(), ['adam', 'LISA', 'barT'])))


# reduce接受list求积
def prod(L):
    return reduce(lambda x, y: x * y, L)


# str2int
def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


# str2float
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)
