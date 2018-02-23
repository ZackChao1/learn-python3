#!/bin/env python3
# -*- coding:utf-8 -*-
"""
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

1. asyncio提供了完善的异步IO支持；

2. 异步操作需要在coroutine中通过yield from完成；

3. 多个coroutine可以封装成一组Task然后并发执行。
"""
import asyncio
import threading
from datetime import datetime

# @asyncio.coroutine
# def hello():
#     print("hello!")
#     # 异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print("等待结束，返回：", r)


# # get EventLoop
# loop = asyncio.get_event_loop()
# # exec coroutine
# loop.run_until_complete(hello())
# loop.close()


"""
@asyncio.coroutine把一个generator标记为coroutine类型
然后，我们就把这个coroutine扔到EventLoop中执行

hello() 首先执行print("hello!")
然后，yield from语法可以让我们方便地调用另一个generator

由于asyncio.sleep()也是一个coroutine
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值(None)，然后继续执行下一行语句

把asyncio.sleep(1)看成是一个耗时1秒的IO操作
此时，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

"""


# 异步hello

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)     # 调用另外一个generator
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()     # 获取消息引用
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# another example
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()