#!/bin/env python3
# -*- coding:utf-8 -*-


# try...except...finally
# 错误是class，捕获一个错误就是捕获到该class的一个实例

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)  # 定义错误
    return 10 / n


# foo('0')


# 捕获自定义错误
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

# raise不带参数转换错误类型
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
