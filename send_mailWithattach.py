#!/bin/env python3
# -*- coding:utf-8 -*-

# 带附件的邮件
# 邮件对象:
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email import encoders
from email.header import Header
from email.mime.text import MIMEText


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





msg2 = MIMEMultipart()
msg2['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg2['To'] = _format_addr('管理员 <%s>' % to_addr)
msg2['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
# attach()
msg2.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open(r'E:\Pictures\背景\wpcache\360wallpaper.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='360wallpaper.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='360wallpaper.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg2.attach(mime)

# 在加入附件的基础上，邮件正文嵌入图片
# 引入cid:x 给图片编号
msg2.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))


# 支持html和plain格式
msg = MIMEMultipart('alternative')
msg['From'] = ...
msg['To'] = ...
msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...


# 发送邮件
import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)  # 交互信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg2.as_string())  # []发给多个人，as_string转为str
server.quit()

# 加密smtp
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# ...
