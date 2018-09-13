# -*- coding:utf-8 -*-

"""

@auther: ZackChao
@file: use_Xpath.py
@time: 3/8/2018 4:41 PM

"""

from scrapy.selector import Selector


body=open('demo.xml','r',encoding='utf-8').read()
print(body)
print(
# 第一个class内容
Selector(text=body).xpath('/html/body/class[1]').extract(),
# 最后一个class内容
Selector(text=body).xpath('/html/body/class[last()]').extract(),
# 最后一个class的name属性文本内容
Selector(text=body).xpath('/html/body/class[last()]/name/text()').extract()
)

# Xpath嵌套,第二个class
subbody=Selector(text=body).xpath('/html/body/class[2]').extract()
print(
# //指当前匹配文档，匹配当前文档中的节点，如下结果一样
Selector(text=subbody[0]).xpath('//name/text()').extract(),
Selector(text=subbody[0]).xpath('//class/name/text()').extract(),
Selector(text=subbody[0]).xpath('//class/sex/text()').extract()
)