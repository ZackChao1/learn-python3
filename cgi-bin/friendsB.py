#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30/2018 3:53 PM
# @Author  : Aries
# @Site    : 
# @File    : friendsB.py
# @Software: PyCharm


import  cgi


header='Content-Type: text/html\n\n'
formHtml='''
    <html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <H3>Friends list for:<I>NEW USER</I></H3>
    <FORM ACTION="friendsB.py">
        <b>Enter your Name:</b>
        <Input type=hidden NAME=action VALUE=edit>
        <INPUT type=text NAME=person VALUE="NEW USER" size=15>
        <P><b>How many friends do you have?</b>
            %s
        </P>
        <input type="submit">
    </FORM>
</body>
</html>
'''

fradio='<Input type=radio name=howmany value="%s" %s>%s\n'

def showForm():
    friends=[]
    for i in (0,10,25,50,100):
        checked=''
        if i==0:
            checked='CHECKED'
            friends.append(fradio % (str(i),checked,str(i)))

    print('%s%s' % (header,formHtml %''.join(friends)))


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

def doResults(who,howmany):
    print(header+resHTML%(who,who,howmany))

def process():
    form=cgi.FieldStorage()
    if 'person' in form:
        who=form['person'].value
    else:
        who='NEW USER'

    if 'howmany' in form:
        howmany=form['howmany'].value
    else:
        howmany=0

    if 'action' in form:
        doResults(who,howmany)
    else:
        showForm()

if __name__=='__main__':
    process()


