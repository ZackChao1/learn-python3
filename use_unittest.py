#!/bin/env python3
# -*- coding:utf-8 -*-


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attrobute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 单元测试Dict类

import unittest


class TestDict(unittest.TestCase):  # 从unittest.TestCase继承

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言函数返回结果和期望结果
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 断言期待抛出指定类型的Error
            value = d['empty']

    def test_attrerror(self):  # 断言期待抛出AttributeError
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):  # 调用一个测试方法前被执行
        print('setUp')

    def setDown(self):  # 调用一个测试方法后被执行
        print('setDown')


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade1(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'

    def get_grade(self):
        if 80 <= self.score <= 100:
            return 'A'
        elif 60 <= self.score < 80:
            return 'B'
        elif 0 <= self.score < 60:
            return 'C'
        else:
            raise ValueError


# 测试类Student
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


# __name__的两种情况：
# 脚本直接运行__name__等于__main__
# improt调用__name__等于模块名称
if __name__ == '__main__':  # 判断是否作为脚本执行
    import unittest
    unittest.main()
