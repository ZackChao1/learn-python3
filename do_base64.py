#!/bin/env python3
# -*- coding:utf-8 -*-

# 64个字符表示binnary数据
import base64

# 不足用==补充
print(base64.b64encode(b'binary\x00string'),
      base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
      )
# +/和-_互变
print(
    base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'),
    base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
)
# example1
s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)


# example2
def safe_base64_decode(s):
    for i in range(len(s) % 4):
        if isinstance(s, bytes):
            s = s + b'='
        else:
            s = s + '='
    return base64.b64decode(s)


if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
