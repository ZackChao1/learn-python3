#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个盘子从a移动到b上  
        move(1, a, b, c)  # 将最底下的最后一个盘子从a移动到c上 
        move(n - 1, b, a, c)  # 将b上的n-1个盘子移动到c上


move(4, 'A', 'B', 'C')
