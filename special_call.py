#!/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):  # 定义__call__()方法，使实例可直接被调用
        print('My name is %s.' % self.name)


s = Student('Zzc')
s()  # 对实例直接调用

# callable()函数，判断一个对象是否是“可调用”对象

print(
    callable(Student('Zzc')),
    callable(max),
    callable([1, 2, 3]),
    callable(None),
    callable('str')
)
