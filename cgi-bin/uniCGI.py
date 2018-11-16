#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/31/2018 9:33 AM
# @Author  : Aries
# @Site    : 
# @File    : uniCGI.py
# @Software: PyCharm


CODEC='utf-8'
UNICODE_HELLO= (u'\n'
                u'Hello!\n'
                u'\u001AlHola!\n'
                u'\u4F60\u597D!\n'
                u'\n3053\u3093\u306B\u3061\u306F!')

print('Content-Type: text/html; charset=%s \r' % CODEC)
print('\r')
print('<HTML><HEAD><TITLE>Unicode CGI Demo</TITLE></HEAD>')
print('<BODY>')
print(UNICODE_HELLO.encode(CODEC))
print('</BODY></HTML>')
