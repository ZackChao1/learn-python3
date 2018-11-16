#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/1/2018 3:20 PM
# @Author  : Aries
# @Site    : 
# @File    : use_wsgi.py
# @Software: PyCharm


from io import StringIO
import sys
from wsgiref.simple_server import make_server



def simple_wsgi_app(environ,start_response):
    status='200 OK'
    headers=[('Content-Type','text/plain')]
    start_response=(status,headers)
    return [b'Hello world!']

def un_wsgi_app(app,environ):
    body=StringIO.StringIO()

    def start_respone(status,headers):
        body.write('Status:%s\r\n' % status)
        for header in headers:
            body.write('Status: %s\r\n' % header)
        return body.write

    iterable=app(environ,start_respone)
    try:
        if not body.getvalue():
            raise RuntimeErrpr("start_response() not called by app!")
        body.write('\r\n%s\r\n ' %' \r\n'.join(line for line in iterable))
    finally:
        if hasattr(iterable,'close') and callable(iterable.close):
            iterable.close()

    sys.stdout.write(body.getvalue())
    sys.stdout.flush()


httpd=make_server('',8000,simple_wsgi_app)
print('Started app serving on port 8000...')
httpd.serve_forever()