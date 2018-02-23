#!/usr/bin/env python3
# ! -*- coding:utf-8 -*-

from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:  # iter each key
    print(key)
for v in d.values():  # iter each value
    print(v)
for k, v in d.items():  # iter both key and value
    print(k, v)
for ch in 'Zzc':  # iter str
    print(ch)
for x in [1, 2, 3, 4, 5]:  # iter list
    print(x)
print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


def g():
    yield 1
    yield 2
    yield 3


# 判断对象是否可iter
print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterable))
print('Iterator? \'abc\':', isinstance('abc', Iterable))
print('Iterator? 123:', isinstance(123, Iterable))
print('Iterator? g():', isinstance(g(), Iterable))

for i, value in enumerate(['Z', 'z', 'c']):  # iter list with index
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:  # iter complex list
    print(x, y)


def findMinAndMax(L):
    if len(L) == 0:     # 边界条件
        return None, None
    if len(L) == 1:
        return L[0], L[0]
    min = L[0]
    max = L[0]
    for v in L:
        if v > max:
            max = v
        if v < min:
            min = v
    return min, max




# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
