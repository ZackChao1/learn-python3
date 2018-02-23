#!/bin/env python
# -*- coding:utf-8 -*-

import functools


# 定义decorator
def log(func):
    def wrapper(*args, **kw):  # 接受任意参数的调用
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper  # 返回一个函数


@log  # now = log(now)，同名的now指向了新的函数
def now():
    print('2015-12-19')  # 先调用装饰的函数，在调用原始函数


print(now())
print(now.__name__)  # 此时now的name已变为返回函数wrapper


# 定义decorator带参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('执行')  # now=log('执行')(now)
def now():
    print('2017-12-19')


print(now())
print(now.__name__)  # 此时now的name已变为返回函数wrapper


def log(func):
    @functools.wraps(func)  # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log3(text):
    def decorator(func):
        @functools.wraps(func)  # wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3('执行')  # now=log('执行')(now)
def now3():
    print('2017-12-19')


print(now3())
print(now3.__name__)
