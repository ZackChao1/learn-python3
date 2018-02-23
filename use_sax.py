#!/bin/env python3
# -*- coding:utf-8 -*-

# XML parse
# DOM vs SAX（萨克斯）
# SAX响应事件

from xml.parsers.expat import ParserCreate
import string

class DefaultSaxHandler(object):  # 如何重载的？
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 拼XML结构
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('some & data'.encode('utf-8'))
L.append(r'</root>')
for x in L:
    print(x)


# example query weather
# 利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报
from xml.parsers.expat import ParserCreate
from urllib import request
import time
class DefaultSaxHandler(object):
    def __init__(self):
        self.location = {}
        self.forecast = []
    def start_element(self, name, attrs):   # SAX start事件处理
#         print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.location = attrs
        if name == 'yweather:forecast':
            data = {}
            date = time.strftime('%Y-%m-%d' , time.strptime(attrs['date'],'%d %b %Y'))
            data['date'] = date
            data['high'] = attrs['high']
            data['low'] = attrs['low']
            self.forecast.append(data)

    def end_element(self, name):
        pass
    def char_data(self, text):
        pass

def parseXml(xml_str):      # sax解析
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return {
        'city': handler.location['city'],
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:  # 获取天气预报接口
    data = f.read()

result = parseXml(data.decode('utf-8'))     # 解析结果
assert result['city'] == 'Beijing'
print('ok')
