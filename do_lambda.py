#!/bin/env python3
# -*- coding:utf-8 -*-

# 匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 利用变量调用匿名函数
f = lambda x: x * x
print(f)
print(f(4))


# 匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y


r = build(1, 2)     #匿名函数也是函数对象，调用前赋值给var
print(r())
print(build(3,4)())     #不赋值需写成build(3,4)()

print(list(filter(lambda x: x % 2 == 0, range(1, 20))))
