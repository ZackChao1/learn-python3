#!/bin/env python3
# ! -*- coding:utf-8 -*-
import sys

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))  # [] ()区分
print(g)
print(next(g))
print(next(g))
print(next(g))  # 一个一个的调用generator,没有更多的元素时，抛出StopIteration的错误
for n in g:  # 不需要关心StopIteration的错误
    print(n)


def fib(max):  # 斐波拉契数列的推算规则函数
    n1, a, b = 0, 0, 1
    while n1 < max:
        print(b)
        a, b = b, a + b  # a=b,b=a+b
        print(n1, 'a=%s' % a, 'b=%s' % b)
        n1 = n1 + 1
    return 'done'


print(fib(10))


def fib(max):  # 函数中包含yield则是一个generator对象
    n1, a, b = 0, 0, 1
    while n1 < max:
        yield b  # 每调用next()一次，遇到yield就返回
        a, b = b, a + b
        print(n1, 'a=%s' % a, 'b=%s' % b)
        n1 = n1 + 1
    return 'done'


print(fib(20))  # is generator


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield (5)


print(next(odd()))
print(next(odd()))
print(next(odd()))  #每次print都生成一个

o = odd()   #o指向generator
print(next(o))  # first     print o指向的generator
print(next(o))  # second
print(next(o))  # third     use next()获取generator返回值


# g = fib(6)
# while true:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break
#
# print(g)


# 打印杨辉三角
def angel(n2):
    L = [1]  # 定义一个list[1]
    while True:
        yield L  # 打印出该list
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]  # 计算下一行中间的值（除去两边的1）
        L.insert(0, 1)  # 在开头插入1
        L.append(1)  # 在结尾添加1
        if len(L) > 10:  # 仅输出10行
            break


# 生成一个generator对象，然后通过for循环迭代输出每一行
a = angel(10)
for i in a:
    print(i)
