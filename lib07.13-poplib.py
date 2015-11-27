'''
poplib 模块

poplib 模块提供了一个 Post Office Protocol
( POP3 协议) 客户端实现. 这个协议用来从邮件服务器 "pop" (拷贝) 信息到
你的个人电脑.
'''
# 使用 poplib 模块
import poplib
import random
import os

SERVER = 'pop.spam.egg'

USER = 'mulder'
PASSWORD = 'trustnol'
# connect to server
server = poplib.POP3(SERVER)
# login
server.user(USER)
server.pass_(PASSWORD)
# list items on server
resp, items, octets = server.list()

# download a random message
id, size = string.split(random.choice(items))
resp, text, octets = server.retr(id)

text = string.join(text, "\n")
file = StringIO.StringIO(text)

message = rfc822.Message(file)
for k, v in message.items():
	print( k, "=", v)
print(message.fp.read())



