#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/18/2018 3:52 PM
# @Author  : Aries
# @Site    : 
# @File    : use_win32_word.py
# @Software: PyCharm


from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import  win32com.client as win32

warn=lambda app: showwarning(app,'Exit?')
RANGE=range(3,8)

def word():
    app='Word'
    word=win32.gencache.EnsureDispatch('%s.Application' % app)
    doc=word.Documents.Add()
    word.Visible=True
    sleep(1)

    rng=doc.Range(0,0)
    rng.InsertAfter('Python-to%s Test \r\n\r\n' % app)
    sleep(1)
    for i in RANGE:
        rng.InsertAfter('Line%d\r\n\r\n' %i)
        sleep(1)
    rng.InsertAfter("\r\nTh-th-th-that's all folks!\r\n")

    warn(app)
    doc.Close(False)
    word.Application.Quit()

def ppoint():
    app='PowerPoint'
    ppoint=win32.gencache.EnsureDispatch('%s.Application' % app)
    pres=ppoint.Presentations.Add()
    ppoint.Visible=True

    sl=pres.Slides.Add(1,win32.constants.ppLayoutText)      #  主标题
    sleep(1)
    sla=sl.Shapes(1).TextFrame.TextRange        # 文本部分
    sla.Text='Python-to-%s Demo' % app
    sleep(1)
    slb=sl.Shapes(2).TextFrame.TextRange
    for i in RANGE:
        slb.InsertAfter("\r\nTh-th-th-that's all folks!")

    warn(app)
    pres.Close()
    ppoint.Quit()


def outlook():
    app='outlook'
    olook=win32.gencache.EnsureDispatch('%s.Application' % app)

    mail=olook.CreateItem(win32.constants.olMailItem)
    recip=mail.Recipients.Add('You@127.0.0.1')
    subj=mail.Subject='Python-to-%s Demo' %app
    body=["Line %d" % i for i in RANGE]
    body.insert(0,'%s\r\n' % subj)
    body.append("\r\n Th-th-th-that's all folks!")
    mail.Body='\r\n'.join(body)
    mail.Send()

    ns=olook.GetNamespace("MAPI")
    obox=ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()

    warn(app)
    olook.Quit()



if __name__=='__main__':
    Tk().withdraw()

    ppoint()
    outlook()


