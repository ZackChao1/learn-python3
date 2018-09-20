#!/bin/env python3
# -*- coding:utf-8 -*-

import re

# match() 匹配、切分字符串
s = r'ABC\\-001'
x = re.match(r'^\d{3}-\d{3,8}$', '010-123456')  # match对象
print(x)

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

bt='bat|bet|bit'
m=re.match(bt,'bat')    # m is regex object
if m is not None: m.group()


print('a b  c'.split(' '))  # 切分字符串,法切分空格
print(re.split(r'\s+', 'a b   c'))  # re灵活
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c   d'))
print(re.split(r'[\s\,\;]+', 'a;b;; c  d'))

# search() 搜索匹配
m=re.search('foo','eatfood')
if m is not None: m.group()


# group() 提取子字符串
# 识别合法电话号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m,
      m.group(0),
      m.group(1),
      m.group(2),
      m.group()
      )

m=re.match('(a(b))','ab')
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


# findall()
m=re.findall('cat','carry the barcardi to the car')

# finditer() 相比findall 节省内存
s='This  and that.'
m=re.finditer(r'(th\w) and (th\w+)',s,re.I)
m=[g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s,re.I)]

# 单分组多重匹配
it=re.finditer(r'(th\w+)',s,re.I)
g=it.next()
print(g.groups())



# 解析器
DATA=(
    'Mountain View,CA 94040',
    'Sunnyvale,CA',
    'Los Altos,94023',
    'Cupertino 95014',
    'Palo Alto CA'
)
for datum in DATA:
    print(re.split(', |(?= (?:\d{5} |[A-Z]{2}))',datum))







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

# kinds of matching
'''
    ^(bat|bit|but|hat|hit|hut)      [bh][aiu]
    \w+\w+
    \w+,\s\w+
    [A-Za-z-]+[\w_]+
    (\w+)*\w*
    w{3}\.\w+\.(edu|com|net)
    \d+
    \d+[1L]
    \d+(\.\d*)?
    [-]?\d+(\.\d*)?[+-][-]?\d+(\.\d*)?[Jj]
    (\w+\.)?\w+@\w+\.\w+
    (http://)?(w{3}\.)?\w+\.com
    (\w+)
    1[012]
    (\d{4}-\d{6}-\d{5})|(\d{4}-\d{4}-\d{4}-\d{4})
    
'''
# gendata.py
def check(card):
    contexts=re.search(r'\d{4}-(\d+)-(\d+)-(\d+)(?:-(\d{4})',card).groups()
    if not contexts[2] and len(contexts[0])==6 and len(contexts[1])==5:
        return True
    elif contexts[2] and len(contexts[0])==4 and len(contexts[1])==4 and len(contexts[2])==4:
        return True
    else:
        return False
# redata.tex
def Count(filename):
        weeks={

        }
        with open(filename) as f:
            contexts=f.read()
            result=re.findall(r'(\w{3})\s\w{3}',contexts)
            for i in result:
                weeks[i]=weeks.get(i,0)+1

        return wekks
# email domain replace
def Replace(filename,mail):
    with open(filename) as f:
        contexts=f.read()
        replace=re.sub(r'\w*@\w*\.\w{3}',mail,contexts)
        print(replace)

# print time
def print_time(filename):
    with open(filename) as f:
        contexts=f.read()
        time=re.findall(r'\s(\s{3})\s(\d{2}).*(\d{4})',contexts)
        for t in time:
            print(','.join(t))

