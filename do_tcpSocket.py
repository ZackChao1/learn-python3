#!/bin/env python3
#   -*- coding:utf-8 -*-

# socket library
import socket

'''
    1、创建客户端socket
    2、尝试连接服务器
    3、通信循环
    4、发送、接收
    5、关闭客户端socket
'''

# tsTclint.py
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket.socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=input('>')
    if not data:
        break
    tcpCliSock.send(data)

    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()



'''
   1、创建服务器socket
   2、socket绑定地址
   3、监听连接
   4、服务器无限循环
   5、接受客户端连接
   6、通信循环
   7、接收、发送
   8、关闭客户端socket
   9、关闭服务端socket
'''

# tsTserv3.py
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket.socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection....')
    tcpCliSock,addr=tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (bytes(ctime(),'utf-8'),data))
    tcpCliSock.close()
tcpSerSock.close()



# Client创建一个socket
# AF_INET ipv4协议 socket家族
# SOCK_STREAM 面向流的TCP协议 socket类型
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))  # argument is a tuple
# 发送请求
# TCP连接双向通道
# 格式符合HTTP标准
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# 接收数据
buffer = []
while True:
    d = s.recv(1024)  # 每次接收1k字节
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)  # 连接bytes

# 关闭连接
s.close()

# 处理bytes
header, html = data.split(b'\r\n\r\n', 1)  # 分割一次 本行bytes\r\n\r\n<!DOCTYPE html><!--STATUS
print(header.decode('utf-8'))  # byetes to str
with open(r'E:\Material\2-Development\Python\Python code\learn-python3\baidu.html', 'wb') as f:
    f.write(html)




# Server创建socket
# IPV4的TCP协议Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了
s.bind(('127.0.0.1', 9999))  # bind() port ,argment is tuple
s.listen(5)  # 监听端口连接最大数
print('Wating for connection...')
# 线程处理
import time
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 处理请求
import threading
while True:
    sock, addr = s.accept()  # accept()接收连接
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 创建新线程来处理tcp连接，单线程无法处理其他连接
    t.start()




# 服务端测试

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
