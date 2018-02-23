#!/bin/env python3
# -*- coding:utf-8 -*-


class Hello1(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello1()
h.hello()


# type()动态创建类
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 动态创建Hello class
h = Hello()
h.hello()
