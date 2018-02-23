#!/bin/env python3
# -*- coding:utf-8 -*-


# 返回求和函数
def lazy_sum(*args):
    def sum3():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum3


# 调用返回函数,注意添加函数括号
print(lazy_sum(1, 3, 5, 7, 9))
print(lazy_sum(1, 3, 5, 7, 9)())

# 调用返回函数，相同参数返回函数都不同，互不影响
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
# 返回函数并非立即执行，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs  # 迭代完f()执行完后返回fs,fs为9


f1, f2, f3 = count1()
print(f1(), f2(), f3())


# 返回函数中引用循环变量
def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count2()
print(f1(), f2(), f3())


# use generator
def createCounter1():
    def f():
        n = 0
        while True:
            n += 1
            yield n  # 先创造一个生成器

    sum1 = f()

    def counter():
        return next(sum1)  # 用一个函数来调用生成器

    return counter


M1 = createCounter1()
print(M1())  # 注意这里的调用返回函数
print(M1())
print(M1())

# use list
def createCounter2():
    fs = [0]

    def counter():
        fs[0] = fs[0] + 1
        return fs[0]

    return counter


M2 = createCounter2()
print(M2())
print(M2())
print(M2())


# 使用nonlocal关键字，将局部变量变成全局变量
def createCounter3():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


M3 = createCounter3()
print(M3())
print(M3())
print(M3())