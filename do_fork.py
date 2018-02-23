#!/usr/env python3
# -*- coding:utf-8 -*-

# os module system call
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid=os.fork()
if pid==0:
    print('I am child process (%s) and my parent is %s.'%(os.getpid(),os.getpid()))
else:
    print('I(%s) just created a child process(%s)'%(os.getpid(),pid))
    