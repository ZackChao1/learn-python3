#!/bin/env python3
# -*- coding:utf-8 -*-

#Posix Thread
#_thread and threading module
import time, threading

# 新线程执行的代码:
# MainThread
# LoopThread子线程
# Thread-1、Thread-2
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)