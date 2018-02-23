#!/bin/env python3
# -*- coding:utf-8 -*-

import re

# match 匹配、切分字符串
s = r'ABC\\-001'
x = re.match(r'^\d{3}-\d{3,8}$', '010-123456')  # match对象
print(x)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

print('a b  c'.split(' '))  # 切分字符串,法切分空格
print(re.split(r'\s+', 'a b   c'))  # re灵活
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c   d'))
print(re.split(r'[\s\,\;]+', 'a;b;; c  d'))

# Group 提取子字符串
# 识别合法电话号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m,
      m.group(0),
      m.group(1),
      m.group(2),
      m.group()
      )

# 识别合法的时间
t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups())

# 贪婪匹配
x = re.match(r'^(\d+)(0*)$', '102300').groups()
# 加入？非贪婪匹配
y = re.match(r'^(\d+?)(0*)$', '102300').groups()

# compile()
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 编译
re_telephone.match('010-12345').groups()  # 调用正则
re_telephone.match('010-8086').groups()  # 调用正则


# match eamil addr
def is_valid_email(addr):
    if re.match(r'[a-zA-z_.]*@[a-aA-Z.]*', addr):
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# match email head
def name_of_email(addr):
    r = re.compile(r'^(<?)([\w\s]*)(>?)([\w\s]*)@([\w.]*)$')
    if not r.match(addr):
        return None
    else:
        m = r.match(addr)
        return m.group(2)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
