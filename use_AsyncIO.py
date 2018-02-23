#!/bin/env python3
# coding=utf-8

# -*- coding：utf-8 -*-

# 同步IO模型
# do_some_code()
#f = open('/path/to/file', 'r')
#r = f.read()  # <== 线程停在此处等待IO操作结果
# IO操作完成后线程才能继续执行:
# do_some_code(r)




# 异步IO模型
# 消息模型，“读消息--处理消息”
#loop = get_event_loop()
#while True:
#    event = loop.get_event()
#    process_event(event)


import asyncio

@asyncio.coroutine  # 标记 为coroutine类型
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

# another example
import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
