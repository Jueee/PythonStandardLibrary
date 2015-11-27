'''
nntplib 模块

nntplib 模块提供了一个网络新闻传输协议( Network News Transfer Protocol,
NNTP )客户端的实现.
'''
# 使用 nntplib 模块列出消息
# 从新闻服务器上读取消息之前, 你必须连接这个服务器并选择一个新闻组.
# 以下会从服务器下载一个完成的消息列表, 然后根据列表做简单的统计.
import nntplib

SERVER = "news.spam.egg"
GROUP = "comp.lang.python"
AUTHOR = "fredrik@pythonware.com" # eff-bots human alias

server = nntplib.NNTP(SERVER)
resp, count, first, last, name = server.group(GROUP)
print "count", "=>", count
print "range", "=>", first, last
# list all items on the server
resp, items = server.xover(first, last)
# extract some statistics
authors = {}
subjects = {}
for id, subject, author, date, message_id, references, size, lines in
items:
authors[author] = None
if subject[:4] == "Re: ":
subject = subject[4:]
subjects[subject] = None
if string.find(author, AUTHOR) >= 0:
print id, subject
print "authors", "=>", len(authors)
print "subjects", "=>", len(subjects)
