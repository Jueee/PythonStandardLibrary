'''
imaplib 模块

imaplib 模块提供了一个 Internet Message Access Protocol ( IMAP, Internet
消息访问协议) 的客户端实现. 这个协议允许你访问邮件服务器的邮件目录,
就好像是在本机访问一样. 
'''
import imaplib
import random
import io

SERVER = "imap.spam.egg"
USER = "mulder"
PASSWORD = "trustno1"

# connect to server
server = imaplib.IMAP4(SERVER)

# login
server.login(USER, PASSWORD)
server.select()

# list items on server
resp, items = server.search(None, "ALL")
items = string.split(items[0])

# fetch a random item
id = random.choice(items)
resp, data = server.fetch(id, "(RFC822)")
text = data[0][1]

file = io.StringIO(text)
message = rfc822.Message(file)
for k, v in message.items():
	print (k, "=", v)
print(message.fp.read())
server.logout()