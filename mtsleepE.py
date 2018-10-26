#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/29/2018 3:07 PM
# @Author  : Aries
# @Site    : 
# @File    : mtsleepE.py
# @Software: PyCharm

import threading
from time import sleep,ctime


loops=(4,2)

def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'don at:',ctime())

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    def funr(self):
        self.func(*self.args)

def main():
    print('starting at:',ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
        t=MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all DONE at:',ctime())

if __name__=='__main__':
    main()