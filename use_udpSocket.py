#!/bin/env python3
# -*- coding:utf-8 -*-

import socket

# Server创建socket
# IPV4的UCP协议Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口,无需listen()
# udp端口和tcp端口不冲突
s.bind(('127.0.0.1', 9999))
# 处理请求
print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)  # sendto()

# Client创建socket
# IPV4的UCP协议Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))    # sendto()
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
