#!/bin/env python3          #use in Unix/Linux/Mac
# -*- coding:utf-8 -*-      #UTF-8

' a test module '

__author__ = 'Zack Chao'

import sys


def test():
    args = sys.argv  # 获取参数名
    if len(args) == 1:  # 第一个参数永远是该.py文件的名称
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':  # if判断调用，禁止直接调用__name__
    test()


# 把内部逻辑用private函数隐藏
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
