#!/bin/env python3
# -*- coding:utf-8 -*-

try:
    f = open('/path/to/file', 'r')
    f.read()
except Exception as e:
    print(e)
finally:
    if f:
        f.close()



# or
# 上下文管理资源对象
with open('/path/to/file','r') as f:
    f.read()
# 包含__enter__ 和 __exit__方法的类对象可被上下文管理，with
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()


# contextlib 的@contextmanager
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager     # 某段代码执行前后执行特定代码
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


# contextlib 的@closing
# closing()方法把对象变为上下文对象
# 实际上closing（）方法也是经过@contextmanager装饰的generator
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
