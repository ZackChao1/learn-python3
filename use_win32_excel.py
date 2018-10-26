#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/18/2018 3:08 PM
# @Author  : Aries
# @Site    : 
# @File    : use_win32_excel.py
# @Software: PyCharm



from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn=lambda app: showwarning(app, 'Exit?')
RANGE=range(3,8)

def excel():
    app='Excel'
    xl=win32.gencache.EnsureDispatch('%s.Application' % app)
    ss=xl.Workbooks.Add()       # 添加工作簿
    sh=ss.ActiveSheet
    xl.Visible=True
    sleep(1)

    sh.Cells(1,1).Value='Python-to-%s Demo' % app
    sleep(1)
    for i in RANGE:
        sh.Cells(i,1).Value='Line %d' % i
        sleep(1)
    sh.Cells(i+2,1).Value="Th-th-th-that's all folks!"

    warn(app)       # showwarning对话框
    ss.Close(False)
    xl.Application.Quit()

if __name__=='__main__':
    Tk().withdraw()
    excel()
