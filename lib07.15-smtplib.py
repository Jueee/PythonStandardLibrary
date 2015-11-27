'''
smtplib 模块

smtplib 模块提供了一个 Simple Mail Transfer Protocol ( SMTP , 简单邮件
传输协议) 客户端实现. 该协议用于通过 Unix 邮件服务器发送邮件
'''
import smtplib
import sys

HOST = "localhost"
FROM = "effbot@spam.egg"
TO = "fredrik@spam.egg"
SUBJECT = "for your information!"
BODY = "next week: how to fling an otter"
body = "\r\n".join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT,
	"",
	BODY))
print(body)

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], body)
server.quit()