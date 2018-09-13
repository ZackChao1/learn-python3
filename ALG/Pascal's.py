# -*- coding:utf-8 -*-

"""

@auther: ZackChao
@file: Pascal's.py
@time: 3/22/2018 2:28 PM

"""

"""
问题：
求二项式系数表中(杨辉三角)第K层系列数?

思路：
1、把第K行的系数存储在队列中;
2、依次出队K层的系数（每行最后一个1不出队），并推算K+1层系数，添加到队尾，最后在队尾添加一个1，便变成了k+1行。
"""

from collections import deque

def yanghui(k):
    q=deque([1])
    for i in range(k):          # 迭代层数
        for j in range(i):      # 出队次数
            q.append(q.popleft()+q[0])    # 弹出第一个数并加上队列第二个数并赋值到队列末尾
        q.append(1)     # 末尾加1
    return list(q)


result=yanghui(10)
print(result)