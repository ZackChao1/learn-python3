#!/bin/env python3
# -*- coding:utf-8 -*-


# tkinter library
from tkinter import *

# 从Frame派生,父容器
# Frame容纳Widget
# example
class Application_test(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()     # pack()加入到父容器
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')     # Label标签
        self.helloLabel.pack()      # pack()到父容器
        self.quitButton = Button(self, text='Quit', command=self.quit)  # Button标签
        self.quitButton.pack()      # pack()到父容器


app=Application_test()
app.master.title('Hello,World!')    # 设置窗口标题
app.mainloop()      # 主消息循环

# another example
from tkinter import *
import tkinter.messagebox as messagebox     # messagebox包私有命名

class Application_test1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)    # 输入框标签
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'  # 获取输入内容
        messagebox.showinfo('Message', 'Hello, %s' % name)  # Message对话框

app1=Application_test1()
app1.master.title(app1.nameInput.get() or 'World')
app.mainloop()

