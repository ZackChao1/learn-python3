#!/bin/env python3
# -*- coding:utf-8 -*-


# subprocess
import subprocess
# call 外部子进程
print('$ nslookup www.baidu.com')
r=subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)

# 输入到外部子进程
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\nwww.baidu.com\nexit\n')
print(output.decode('utf-8'),err)
print('Exit code:',p.returncode)
