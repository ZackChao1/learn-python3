#!/bin/env python3
# -*- coding：utf-8 -*-

# collections 内建的集合模块

from collections import namedtuple

# namedtuple 自定义tuple对象
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(
    p.x,  # 根据属性引用
    p.y
)

isinstance(p, Point)
isinstance(p, tuple)

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)

# deque 插入和删除操作双向列表
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')  # 定义不存在时默认返回值
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])

# OrderedDict 保持dict的key的顺序
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(d)  # d是无序的
od = OrderedDict([('c', 1), ('a', 2), ('b', 3)])
print(od)

# 按插入的顺序排列
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))


# OrderedDict可以实现一个FIFO（先进先出）的dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter
from collections import Counter

p = Counter()   # 计数器

for str in 'programming':
    p[str]+=1

print(p)