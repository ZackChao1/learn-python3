#!/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))  # 不好看容易暴露实例内部重要数据


# 添加__str__()
class Student1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __str__()返回用户看到的字符串，__repr__()返回程序开发者看到的字符串
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student1('JackChen'))

s = Student1('zzc')
print(s)
