#!/bin/env python3
# -*- coding:utf-8 -*-

import os
from multiprocessing import Process
# Process
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))


if __name__ =='__main__':
    print('Parent process %s.'%os.getpid())
    p=Process(target=run_proc,args=('test',))   # 创建子进程
    print('Child process will start.')
    p.start()
    p.join()    #等待子进程结束后继续执行,用于进程间同步
    print('Child process end.')


