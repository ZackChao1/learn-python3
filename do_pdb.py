#!/bin/env python3
# -*- coding:utf-8 -*-

s = '0'
n = int(s)
print(10 / n)

# $ python -m pdb do_pdb.y
# pdb调试环境
# l 查看代码
# n 单步执行代码
# p 查看变量

# pdb.set_trace()
# 设置断点

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)


