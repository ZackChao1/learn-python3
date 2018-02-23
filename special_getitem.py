#!/bin/env python3
# -*- coding:utf-8 -*-

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[4])
print(list(range(100))[5:10])


# print(f[5:10])  # __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice


class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib1()
print(f[0:5], f[:10])
