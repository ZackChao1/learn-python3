#!/bin/env python3
# -*- coding:utf-8 -*-

import requests

# get(url)
# return response object
response = requests.get("http://www.baidu.com")
print(response.text)
print(response.status_code)
# 从header中猜测的响应的内容编码方式
print(response.encoding)
# 从内容中分析的编码方式（慢）
print(response.apparent_encoding)
print(response.content)

# get(url,headers=)
# 自定义headers
hd = {'User-agent': '123'}
r = requests.get('http://www.baidu.com', headers=hd)
print(r.request.headers)

# get(url,proxies=)
pxs = {'http': 'http://user:pass@10.10.10.1:1234',
       'https': 'https://10.10.10.1:4321'}
r = requests.get('http://www.baidu.com', proxies=pxs)

# request()
# get()
'''
    kwargs: dict、tuple、true、false；
'''


# head()
# post()
# put()
# path()
# delete()

# common getHtmlText

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=80)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong"
