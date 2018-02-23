#!/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self):
        self.name = 'Michael'


s = Student()
print(s.name)


# 定义__getattr__()方法，动态返回一个属性
class Student1(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25  # 返回函数
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student1()
print(s.name, s.score, s.age(), s.abc)  # AttributeError错误


# 链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.use.timeline.list)



