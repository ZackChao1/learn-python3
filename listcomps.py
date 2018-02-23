#!/usr/bin/env python3
# ! -*- coding:utf-8 -*-

import os


print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])  # use the listcomps
print([m+n for m in 'ABC' for n in 'XYZ'])  # listcomps双层循环全排列AX,BY,CZ
print([d for d in os.listdir('.')])     # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])   # use two var with listcomps

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [a.lower() for a in L1 if isinstance(a, str)]      #use if with listcomps

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
