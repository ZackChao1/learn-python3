#!/bin/env python3
# -*- coding:utf-8 -*-

# 处理URL函数，不通方法分别有不同的函数
# 通过装饰器URL和函数自动的关联

from flask import Flask
from flask import request
# Flask自带的server端口5000

# 初始化Flask对象
app = Flask(__name__)


# route() 装饰器把一个函数绑定到对应的 URL 上
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home<h1>'


@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
