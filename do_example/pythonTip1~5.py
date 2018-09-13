#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/6/2018 2:35 PM
# @Author  : Aries
# @Site    : 
# @File    : pythonTip1~5.py
# @Software: PyCharm


# just print a+b
a=3;b=4;print(a+b)

# list sort
L=[2,8,3,50]
for i in range(len(L)-1):       # 注意index范围，从0开始
    if L[i]>L[i+1]:     # 升序列
        L[i],L[i+1]=L[i+1],L[i]
print(L)

L.sort()
print(sorted(L))

# L中取最小的放入s中
x=0;y=len(L)    #  x 循环索引 y循环次数也就是L长度
s=[]    # 需要追加输出的列表
while x<y:
    s.append(min(L))
    L.remove(min[L])
    x+=1
print(s)

# 快排
from functools import filter
def qsort(x):
    if x==[]:
        return []
    return qsort(filter(lambda smaller:smaller<x[0],x))+[x[0]]+qsort(filter(lambda larger:larger>x[0],x))
    # 返回部分有问题

# 字符串逆序
a='12345';print(a[::-1])

for x in range(len(a)):
    print(a[-(x+1)])
# 输出字典a的key
a={1:1,2:2,3:3}
print(','.join(str(n) for n in a.keys()))   # a.keys直接用list comps 列出再join起来

b=a.keys();l=len(b);c=[]    # 拿出a的key 单独遍历再join
for i in range(l):
    c.append(str(b[i]))
print(','.join(c))




# 字符串奇数位置
print(a[::2])

x=''    # 输出获取到的奇数
for i in range(len(a)):
    if i % 2 != 0:
        x+=a[i]     # 满足位置条件连接字符
print(x)






