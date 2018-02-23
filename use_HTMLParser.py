#!/bin/env python3
# -*- coding:utf-8 -*-

# HTMLParser 解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):  # 重载HTML解析器

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
# 调用feed方法，可多次调用
parser.feed('''<html>      
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# example
from html.parser import HTMLParser
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.result = []

        # 临时变量
        self.dict = {}
        self.isHandling = ''

    def handle_starttag(self, tag, attrs):
        # 找到即将开始的会议
        if tag == 'ul' and attrs[0][1] == 'list-recent-events menu':
            self.flag = True
        if self.flag == True:
            # 分别处理title，time，location三个标签
            # print('starttag: %s' % tag)
            if tag == 'a':
                self.isHandling = 'title'
            if tag == 'time':
                self.isHandling = 'time'
            if tag == 'span':
                self.isHandling = 'location'

    def handle_endtag(self, tag):
        if tag == 'ul' and self.flag == True:
            self.flag = False
        if self.flag == True and tag == 'li':
            self.result.append(self.dict)
            self.dict = {}

    def handle_data(self, data):
        if self.isHandling != '':
            self.dict[self.isHandling] = data
            self.isHandling = ''


parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in parser.result:
    for (k, v) in item.items():
        print('%s: %s' % (k, v))
    print('-------------------')
