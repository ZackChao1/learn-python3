# -*- coding:utf-8 -*-

"""

@auther: ZackChao
@file: digital_conversion.py
@time: 3/22/2018 3:12 PM

"""

"""
问题：
对于一对正整数a,b,对a只能进行加1，减1，乘2操作，问最少对a进行几次操作能得到b？
    例如：
        a=3,b=11: 可以通过3*2*2-1，3次操作得到11；
        a=5,b=8：可以通过(5-1)*2，2次操作得到8；
思路：
1、本题用广度优先搜索，寻找a到b状态迁移最短路径，对于每个状态s，可以转换到s+1,s-1,s*2:
2、把初始化状态a入队；
3、出队一个状态s，然后s+1,s-1,s*2入队；
4、反复循环第二步骤，直到状态s为b；
"""

from collections import deque


def atob(a, b):
    """
    :param a: 开始的数字
    :param b: 最终转换之后的数字
    :return: 最小匹配的次数
    """
    q = deque([(a, 0)])  # a=当前数字，0=操作的次数
    checked = {a}  # 已经检查过的数据
    while True:
        s, c = q.popleft()
        if s == b:
            break
        if s < b:  # 要计算的数小于计算之后的数字
            if s + 1 not in checked:  # 如果要计算的数字+1不在已检查过的数据集合中
                q.append((s + 1, c + 1))  # 要计算的数+1，转换次数+1
            checked.add(s + 1)  # 把计算过的数添加到checked集合中
        if s * 2 not in checked:
            q.append((s * 2, c + 1))
            checked.add(s * 2)
        if s > 0:  # 要计算的数大于0
            if s - 1 not in checked:
                q.append((s - 1, c + 1))
            checked.add(s - 1)
        return q.popleft()[-1]      # 返回


result = atob(1, 3)
print(result)
