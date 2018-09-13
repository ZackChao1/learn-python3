#!/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO



# read file
f=open(r'e:\Material\分类.txt','r')
f.read()
f.close()

# readlines()
for line in f.readlines():
    print(line.strip())	#去\n

# read file with IOError
try:
    f = open(r'e:\Material\分类.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# another style
with open(r'e:\Material\分类.txt','rb') as f:
    print(f.read())

# binary file
f=open(r'E:\Pictures\Wow纪念\Hearthstone Screenshot 12-10-17 11.26.13.png','rb')
f.read()

# str encofing
#default is utf-8
f=open(r'e:\Material\分类.txt','r',encoding='GBK',errors='ignore')    # 忽略UnicodeDecodeError
f.read()

# wirte file
f=open(r'e:\Material\分类.txt','a')
f.write('hi')
f.close()   # 缓存起来关闭时写入磁盘
# another method
with open(r'e:\Material\分类.txt','a') as f:
    f.write('str')
    print(f)


