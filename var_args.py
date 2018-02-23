#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def power(x): return x * x  # 位置参数


print(power(99))


def power1(y, n):  # 位置参数(positional argument)
    s = 1
    while n > 0:
        n = n - 1
        s = s * y
        return s


print(5, 2)


def power2(z, n=2):  # 默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * z
        return s


print(5)
print(5, 3)  # 只有与默认参数不符的提供额外参数


def calc0(numbers):  # 不用可变参数
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1     #注意此处return的位置


def calc1(*numbers):  # 可变参数包括0个参数
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n * n
    return sum1     #注意此处return的位置


print(calc0([1, 2, 3]))
print(calc1(1, 2, 3))

test = [1, 2, 3]
print(calc1(test[0],test[1],test[2]))
print(calc1(*test))




def hello(greeting, *args):  # 可变参数
    if len(args) == 0:
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting, ','.join(args)))


hello('Hi')
hello('Hi', 'Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')
names = ('Bart', 'Lisa')
hello('Hello', *names)  # 可变参数，传入tuple
