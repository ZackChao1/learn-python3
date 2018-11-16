#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/31/2018 9:46 AM
# @Author  : Aries
# @Site    : 
# @File    : advCGI.py
# @Software: PyCharm


from cgi import FieldStorage
from os import environ
from urllib.parse import quote,unquote
from io import StringIO


class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = 'AdvCGI.py'

    formhtml = '''
        <HTML>
            <HEAD><TITLE> Advanced CGI Demo</TITLE></HEAD>
            <BODY><H2>Advanced CGI Demo Form</H2>
                <FORM METJOD=post ACTION="%s" ENCTYPE="multipart/form-data">
                <H3>My Cookie Setting</H3>
                <LI> <CODE><B>CPPuser = %s </B></CODE>
                <H3>Enter cookie value<BR>
                <INPUT NAME=cookie value="%s"> (<I>optional</I></H3>
                <H3>Enter your name<BR>
                <INPUT NAME=person VALUE="%s"> (<I>required</I>)</H3>
                <H3>What languages can you program in ?
                (<I>at least one required</i>)</H3> 
                %s
                <H3>Enter file to upload <AMALL>(max size 4k)</SMALL></H3>
                <INPUT TYPE=file NAME=upfile VALUE-"%s" SIZE=45>
                <P><INPUT TYPE=submit>
                </FORM>
            </BODY>
        </HTML>
    '''
    langSet = ('Python','Ruby', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    langItem = '<INPUT TYPE=checkbox NAME=lang VALUE="%s" %s> %s\n'

    errhtml = '''
    <HTML>
    <HEAD><TITLE>Advanced CGI Demo</TITLE></HEAD>
    <BODY>
        <h3>ERROR</h3>
        <b>%s</b>
        <p><form><input type=button value=BackONClick='windows.history.back()"></form></p>
    </BODY>  
    </HTML>
    '''

    reshtml = '''
    <HTML>
    <HEAD>
        <TITLE>
            Advanced CGI Demo (dynamic screen)
        </TITLE>
    </HEAD>
    <BODY>
        <H2>Your uploaded Data</H3>
        <H3>Your cookie value os: <B>%s</B></H3>
        <H3>Your name is: <B>%s</B></H3>
        <H3 You can program in the following languages:</H3>
        <UL>%s</UL>
        <H3>Your uploaded file ...<BR>
        Name: <I>%s</I><BR>
        Contents:</H3>
        <PRE>%s</PRE>
        Click <A Herf="%s"><B>here</B></A> to return to form.
    </BODY><HTML>
    '''

    def getCPPCookies(self):
        if 'HTTP_COOKIE' in environ:
            cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
            print(cookies)
            for eachCookie in cookies:
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])
            if 'info' not in self.cookies:
                self.cookies['info'] = ''
            if 'user' not in self.cookies:
                self.cookies['user'] = ''
        else:
            self.cookies['info'] = self.cookies['user'] = ''
            if self.cookies['info'] != '':
                self.who, langStr, self.fn = self.cookies['info'].split(':')
                self.langs = langStr.split(',')
            else:
                self.who = self.fn = ''
                self.langs = ['Python']

    def showForm(self):
        self.getCPPCookies()

        # put together language checkboxes
        langStr = []
        for eachLang in AdvCGI.langSet:
            langStr.append(AdvCGI.langItem % (eachLang, 'CHECKEN' if eachLang in self.langSet else '', eachLang))

        # see if user cookie set up yet
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<I>(cookie has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        print('%s%s'%(self.header, self.formhtml % (self.url, cookStatus, userCook,userCook, ' '.join(langStr), userCook)))

    def showError(self):
        print(AdvCGI.header + AdvCGI.errhtml % (self.error))

    def setCPPCookies(self):
        # tell client to store cookies
        for eachCookies in self.cookies.keys():
            print('Set-Cookie: CPP%s=%s; path=/' % (eachCookies, quote(self.cookies[eachCookies])))

    def doResults(self):
        # display results page
        MAXBYTES = 4096
        langList = ''.join(
            '<LI>%s<BR>' % eachLange for eachLange  in self.langs)
        filedata = self.fp.read(MAXBYTES)
        if len(filedata) == MAXBYTES and f.read():
            filedata = '%s%s' % (filedata, '...<B><I>(file truncated due to size)</I></B>')
            self.fp.close()
        if filedata == '':
            filedata = '<B<<I>(file not given or upload error)</I></B>'
        filename = self.fn

        # see if user cookie set up yet
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<I>(cookie has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        # set cookies
        self.cookies['info'] = ':'.join((self.who, ','.join(self.langs, ','), filename))

        print(
            '%s%s' % (AdvCGI.header, AdvCGI.reshtml % (cookStatus, self.who, langList, filename, filedata, AdvCGI.url)))

    def go(self):
        # determine which page to return
        self.cookies = {}
        self.error = ''
        form = FieldStorage()

        # handler pageData from client
        if not form.keys():
            self.showForm()
            return

        if 'person' in form:    # 取person给self.who
            self.who = form['person'].value.strip().title()
            if self.who == '':
                self.error = 'Your name is required.(blank)'
        else:
            self.error = 'Your name is required.(missing)'

        self.cookies['user'] = unquote(form['cookie'].value.strip()) if 'cookie' in form else ''    # 取cookie给self.cookies

        if 'lang' in form:      # 取lang给self.langs
            langData = form['lang']
            if isinstance(langData, list):
                self.langs = [eachLang.value for eachLang in langData]
            else:
                self.langs = [langData.value]
        else:
            self.error = 'At least one language required.'

        if 'upfile' in form:    # 取upfile的filename和file分别给self.fn和self.fp
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no file')
            self.fn = ''

        if not self.error:  # self.error处理
            self.doResults()
        else:
            self.showError()


if __name__ == '__main__':
    page = AdvCGI()
    page.go()
