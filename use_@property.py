#!/bin/env pthon3
# -*- coding:utf-8 -*-


class Student(object):

    @property  # 把score属性变成方法
    def score(self):
        return self._score

    @score.setter  # 把setter方法变成属性
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # 避免属性暴露和检查参数
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999
