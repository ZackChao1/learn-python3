#!/bin/env python3
# -*- coding:utf-8 -*-


# eamil构造MIMEText对象，即邮件主体
# plain纯文本
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')

# smtp发送email
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')


# 处理邮件头
# parseaddr() 解析email地址
# formataddr() 格式化eamil地址
# Header()  邮件头编码
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发件人
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)  # str
# 收件人
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# 主题
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)  # 交互信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  # []发给多个人，as_string转为str
server.quit()

# HTML邮件
# MIMEText对象
# html
msg1 = MIMEText('<html><body><h1>Hello</h1>' +
                '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                '</body></html>', 'html', 'utf-8')

