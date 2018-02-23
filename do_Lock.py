#!/bin/env python3
# -*- coding:utf-8 -*-


#多线程中，所有变量都由所有线程共享
import time,threading
# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)      # 线程调度由操作系统决定，t1、t2交替进行，balance结果不一定是0


# threading.Lock()
# 不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
# 导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
# GIL锁：Global Interpreter Lock
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁,否则称为死线程:
            lock.release()