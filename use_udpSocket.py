#!/bin/env python3
# -*- coding:utf-8 -*-

import socket

'''
    1、创建客户端套接字
    2、通信循环
    3、发送、接收
    4、关闭套接字
'''

# tsUclnt.py
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCliSock=socket.socket(Af_INET,SOCK_STREAM)
while True:
    data=input('>')
    if not data:
        break
    udpCliSock.send(data,ADDR)

    data,ADDR=udpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)
udpCliSock.close()

'''
    1、创建服务端套接字
    2、绑定服务端套接字
    3、通信循环
    4、接收、发送
    5、关闭套接字
'''

# tsUserv.py
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket.socket(AF_INET,SOCK_STREAM)
udpSerSock.bind(ADDR)
while True:
    print('waiting for meassage...')
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s]%s' %(ctime(),data),addr)
    print('...received from and returned to:',addr)
udpSerSock.close()


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



