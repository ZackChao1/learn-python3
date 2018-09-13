#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/30/2018 10:03 AM
# @Author  : Aries
# @Site    : 
# @File    : use_OALogin.py
# @Software: PyCharm

# conda install -c simonflueckiger tesserocr





#import cookielib3
from http import cookiejar
import urllib,requests

loginUrl='http://10.108.32.61/OAWeb/Index.aspx'
imgUrl='http://10.108.32.61/OAWeb/Common/VerifyImage.aspx'

header={
    'Host' : '10.108.32.61',
    'Cache-Control':'max-age=0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://10.108.32.61/OAWeb/Index.aspx',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language ' : 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive'
}

postData={
    '__VIEWSTATE':'',
    '__EVENTVALIDATION':'',
    'txtUser':'luoyingkai',
    'txtPass':'ABcd1234',
    'txtCode':'',
    'ImageButton.x':'',
    'ImageButton.y':'',
    'txtLogonFlag':'0'
}
res=requests.get("http://10.108.32.61")
print(res.cookies)





















# 构造post数据






