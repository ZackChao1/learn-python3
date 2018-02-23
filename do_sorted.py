#!/bin/env python3
# -*- coding:utf-8 -*-


# sorted list
print(sorted([36, 5, -12, 9, -21]))

# 可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 排序字符串
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反序排列
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
