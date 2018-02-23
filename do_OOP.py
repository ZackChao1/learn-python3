#!/bin/env python3
# -*- coding:utf-8 -*-

# procedure-oriented
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


# Object oriented
# 用面向对象的程序设计思想,思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象,定义对象的类
# 对象拥有name和score这两个属性（Property）
class Student(object):  # 从object Class继承

    def __init__(self, name: object, score: object) -> object:
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# 创建该Student类的实例对象bart、lisa，调用对象的方法（Method）发送消息
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)


# definition Class
class Student_test(object):  # 从object Class继承
    pass


# 创建类的实例
bart = Student(1, 2)  # Student object
print(bart, Student)  # 每个object的地址都不一样，而Student本身则是一个类。

# 调用对象
bart.name = 'zzc'
print(bart.name)
print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())


# 实例变量限制
class Student_limit(object):

    def __init__(self, name, score):
        self.__name = name  # 限制外部访问name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)


# print(bart.__name)


# 访问受限
class Student_limit(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


# 继承
# Subclass BaseClass SuperClass
# fist example

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog1(Animal):
    pass


class Cat1(Animal):
    pass


dog = Dog1()
dog.run()
cat = Cat1()
cat.run()


# second example
class Dog2(Animal):

    def run(self):  # overrides method
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat2(Animal):

    def run(self):  # overrides method
        print('Cat is running...')


dog = Dog2()
dog.run()
cat = Cat2()
cat.run()

# 多态
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog2()  # c是Dog类型
isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog2)
isinstance(c, Animal)  # it is true ,c还是Animal类型或者子对象，反之不行


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog2())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

# 获取对象信息
import types

# 判断对象类型
print(type(123),
      type(None),
      type(a),
      type(abs),
      type(123) == type(456),
      type(123) == int,
      type('abc') == type('123')
      )


# 判断对象是否是函数
def fn():
    pass


print(
    type(fn) == types.FunctionType,
    type(abs) == types.BuiltinFunctionType
)

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
a = Animal()
d = Dog1()
print(
    isinstance(d, Dog1),
    isinstance(d, Animal),
    isinstance('a', str),
    isinstance((1, 2, 3,), (list, tuple))  # 判断是否是list或tuple
)

# dir()获取对象属性和方法

print(
    dir('ABC'),
    len('ABC'),  # 'ABC'.__len__()
    'ABC'.__len__(),
    'ABC'.lower()

)


class MyDog(object):
    def __len__(self):  # 自定义__len__
        return 100


dog = MyDog()

print(len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'
print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())
