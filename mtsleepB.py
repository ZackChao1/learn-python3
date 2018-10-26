#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/29/2018 2:22 PM
# @Author  : Aries
# @Site    : 
# @File    : mtsleepB.py
# @Software: PyCharm


import thread
from time import sleep,time

loops=[4,2]

def loop(nloop,nsec,lock):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'don at:',ctime())
    lock.release()

def main():
    print('starting at:',ctime())
    locks=[]
    nloops=range(len(loops))

    for i in nloops:
        lock=thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        thread.start_new_thread(loop(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass

    print('all DONE at:',ctime())

if __name__=='__main__':
    main()
