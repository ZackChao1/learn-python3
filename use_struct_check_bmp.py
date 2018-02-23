#!/bin/env python3
# -*- coding:utf-8 -*-

# struct module bytes和binary数据类型转换
import struct
print(
    struct.pack('>I',10240099),
    struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
)

# check bmp 30bytes
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(
    struct.unpack('<ccIIIIIIHH',s)
)

