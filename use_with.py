#!/bin/env python3
# -*- coding:utf-8 -*-



# with 的用法
class Test(object):
    def __enter__(self):
        print("In __enter__()")
        return "test_with"

    def __exit__(self, type, value, trace):
        print("In __exit__()")


def get_example():
    return Test()


with get_example() as example:
    print("example:", example)