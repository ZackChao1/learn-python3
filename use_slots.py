#!/bin/env python3
# -*- coding:utf-8 -*-


# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误
class Student(object):
    count = 0
    name1 = 'Student'  # Student类本身绑定属性

    def __init__(self, name):
        self.name = name
        Student.count += 1


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


def set_score(self, score):  # 定一个函数作为类的方法
    self.score = score


s = Student('Bob')
s.score = 90  # 给实例绑定属性
t = Student('zzc')
x = Student('zj')
print(s.score, t.name, x.name1, s.count)

from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法,对另一个实例是不起作用的
s.set_age(25)
print(s.age)

Student.set_score = set_score  # 给Student绑定方法,所有实例都可调用
s.set_score(100)
print(s.score)


# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义当前类允许绑定的属性名称


z = Student()

s.name = 'zzc'
s.age = 25
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99  # score不允许绑定
except AttributeError as e:
    print('AttributeError:', e)


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 999
print('g.score =', g.score)
