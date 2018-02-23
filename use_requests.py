#!/bin/env python3
# -*- coding：utf-8 -*-

import requests

# Get()
r = requests.get('https://www.douban.com/')
print(
    r.status_code,
    r.text
)

# with params
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url,  # 实际请求的URL
      r.encoding,  # 自动检测编码
      r.content  # 获取bytes对象
      )

# 特定对象的响应，json
r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

# 传入headers 参数
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

# post请求
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})
'''
params = {'key', 'value'}
r = requests.post(url, json=params) # 自动序列化为json
'''

# 上传文件,读取文件
'''
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
'''
# 获取http响应头
# 获取cookies值

print(r.headers,
    r.headers['Content-Type'],
    r.cookies['ts']
      )
# 传入cookies参数
cs={'token':'12345','status':'working'}
r=requests.get('http://www.baidu.com',cookies=cs,timeout=2.5)

