#!/bin/env python3
# -*- coding:utf-8 -*-

# 先定义metaclass，就可以创建类，最后创建实例
# metaclass允许你创建类或者修改类

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)        #__new(类的对象，类名字，父类集合，方法集合)

class MyList(list,metaclass=ListMetaclass):     # ListMetaclass.__new__()来创建MyList
    pass

L=MyList()
L.add(1)
print(L)

# 普通list是没有add方法
L2=list()
L2.add(1)


