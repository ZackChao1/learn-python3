#!/bin/env python3
# -*- coding:utf-8 -*-



# 定义http处理函数
# http请求所有输入信息都可从environ获取
# http响应所有输出信息都可以通过start_response()
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #return [b'<h1>Hello, web!</h1>']
    return [body.encode('utf-8')]