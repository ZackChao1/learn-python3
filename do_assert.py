#!/bin/env python3
# -*- coding:utf-8 -*-

# assert断言抛出AssertionError
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')


# -o 参数关闭assert
# 把所有assert当成pass来看

