#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30/2018 4:39 PM
# @Author  : Aries
# @Site    : 
# @File    : friendsC.py
# @Software: PyCharm


import  cgi


header='Content-Type: text/html\n\n'
url='/cgi-bin/friendsC.py'
errHtml='''
<HTML>
<HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY>
    <h3>ERROR</h3>
    <b>%s</b>
    <p><form><input type=button value=BackONClick='windows.history.back()"></form></p>
</BODY>  
</HTML>
'''

def showError(error_str):
    print(header+errHtml%error_str)



formHtml='''
    <html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <H3>Friends list for:<I>NEW USER</I></H3>
    <FORM ACTION="%s">
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



def showForm(who,howmany):
    friends=[]
    for i in (0,10,25,50,100):
        checked=''
        if i==0:
            checked='CHECKED'
            friends.append(fradio % (str(i),checked,str(i)))

    print('%s%s' % (header,formHtml %(who,url,who,''.join(friends))))


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
    <P>Click <A href="%s"> here </A> to edit your data again.</P>
</BODY><HTML>
'''

def doResults(who,howmany):
    newUrl=url+'?action=reedit&person=%s&howmany=%s' %(quote_plus(who),howmany)     #
    print(header+resHTML%(who,who,howmany,newUrl))



def process():
    error=''
    form=cgi.FieldStorage()
    if 'person' in form:
        who=form['person'].value.title()
    else:
        who='NEW USER'

    if 'howmany' in form:
        howmany=form['howmany'].value
    else:
        if 'action' in form and form['action'].value=='edit':
            error='Please select number of friedns.'
        else:
            howmany=0

    if not error:
        if 'action' in form and form['action'].value!='reedit':
            doResults(who,howmany)
        else:
            showForm(who,howmany)
    else:
        showError(error)
if __name__=='__main__':
    process()
