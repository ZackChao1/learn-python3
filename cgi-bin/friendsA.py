#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30/2018 3:30 PM
# @Author  : Aries
# @Site    :
# @File    : friendsA.py
# @Software: PyCharm



import cgi

resHTML='''


<HTML>
    <HEAD>
        <TITLE>
            Friends CGI Demo (dynamic screen)
        </TITLE>
    </HEAD>
<BODY>
    <H3>Friends list for : <I> %s </I></H3>
    Your name is : <B> %s </B><P>
    Your have <B> %s </B> friends.
</BODY><HTML>
'''

form=cgi.FieldStorage()
who=form['person'].value
howmany=form['howmany'].value
print(resHTML % (who,who,howmany))

