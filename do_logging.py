#!/bin/env python3
# -*- coding:utf-8 -*-


# 和assert比，logging不会抛出错误，而且可以输出到文件
import logging

s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)


# loggin指定记录信息的级别
# debug
# info
# waring
# error