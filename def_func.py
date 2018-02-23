#!/usr/bin/env python3
# ! -*- coding:utf-8 -*-

import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


n = my_abs(-20)
print('my_abs return', n)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print('x-->y', x, y)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("TypeError, please input number of int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("TypeError, please input number of int or float")
    if not isinstance(c, (int, float)):
        raise TypeError("TypeError, please input number of int or float")
    data = b * b - 4 * a * c
    if data > 0:
        x1 = (-b + math.sqrt(data)) / (2 * a)
        x2 = (-b - math.sqrt(data)) / (2 * a)
        print("the two answers of the equation x1 = {0:.2f}, x2 = {1:.2f}".format(x1, x2))
    elif data == 0:
        x1 = (-b) / (2 * a)
        print("the answers of the equation x1 = x2 = {0:.2f}".format(x1))
    else:
        print("the equation has no answer!")
    return quadratic


print('quadratic is ', quadratic(3, 12, 3))

a = input("请输入一个整数：")
print('hex函数的作用就是把一个整数输出为16进制的字符串')
s = hex(int(a))  # hex()函数
print('hex(%d)=\'%s\'' % (int(a), s))
