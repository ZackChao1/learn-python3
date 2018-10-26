#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/30/2018 2:38 PM
# @Author  : Aries
# @Site    : 
# @File    : tkhello.py
# @Software: PyCharm


from tkinter import *

def resize(en=NONE):
    label.config(font='Helvetica -%d bold' % scale.get())

top=Tk()
top.geometry('250x150')

label=Label(top,text='Hello World!',font='Helvetica -12 bold')
label.pack(fill=X,expand=1)

scale=Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit=Button(top,text='QUIT',command=top.quit,activeforeground='yellow',activebackground='red')
quit.pack()

mainloop()

