#!/bin/env pyrhont3
# -*- coding:utf-8 -*-

# bs4库 是解析、遍历、维护、“标签树“的功能库
from bs4 import BeautifulSoup

# use bs4
html = '''html
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
http://example.com/elsie" class="sister" id="link1">Elsie,
http://example.com/lacie" class="sister" id="link2">Lacie and
http://example.com/tillie" class="sister" id="link3">Tillie;
and they lived at the bottom of a well.</p>
<a> </a>
<p class="story">...</p>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
# html美化转换soup类型
print(soup.prettify())
# 获取各种tag
print(soup.head, '\n',
      soup.title, '\n',
      soup.title.name, '\n',
      soup.title.string, '\n',
      soup.title.parent.name, '\n',
      soup.p, '\n',
      soup.p['class'], '\n',
      soup.a, '\n',
      soup.find_all('a'), '\n',
      soup.find(id="link3"),'\n',
      soup.get_text()
      )
for link in soup.find_all('a'):
    print(link.get('href'))




html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p
"""


# bs4的解析器
# html.parser解析器
# lxml解析器,三方解析器
soup = BeautifulSoup(html_doc, 'lxml')
print('head is ', soup.head)

# 手动设置编码
# soup=BeautifulSoup(markup,from_encoding="编码方式")
# bs4将html转换为python对象
# Tag、NavigableString、BeautifulSoup、Comment

# 搜索tag的
print(soup.head, '\n',
      soup.title, '\n',
      soup.body.b, '\n',
      )

# 获取所有标签
tag = soup.find_all('p')
need = tag[0]

# tag子节点、子孙节点
head_tag = soup.head
print(head_tag.contents)
title_tag = head_tag.contents[0]
print(title_tag)

# .children生成器
for child in title_tag.children:
    print(child)
#
for child in head_tag.descendants:
    print(child)

# tag节点内容
for string in soup.strings:
    print(repr(string))
