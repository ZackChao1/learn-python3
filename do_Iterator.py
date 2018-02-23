#!/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))  # [] {} str 都是Iterable 对象，却不是Iterator对象

print(isinstance(iter([]), Iterator))  # 把[] {} str都变成Iterator使用iter()函数
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))

for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于：
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
