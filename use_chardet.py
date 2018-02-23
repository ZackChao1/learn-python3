#!/bin/env python3
# -*- coding:utf-8 -*-

# chardet 检测编码
import chardet

# detect()
data = '离离原上草，一岁一枯荣'.encode('gbk')
data1 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(
    chardet.detect(b'zzc'),
    chardet.detect(data),
    chardet.detect(data1)
)
