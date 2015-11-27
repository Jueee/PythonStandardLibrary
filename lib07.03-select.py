'''
select 模块

select 模块允许你检查一个或多个 socket , 管道, 以及其他流兼容对象所接受的数据.

可以将一个或更多 socket 传递给 select 函数, 然后等待它们状态改变(可
读, 可写, 或是发送错误信号):
•  如果某人在调用了 listen 函数后连接, 当远端数据到达时, socket 就
成为可读的(这意味着 accept 不会阻塞). 或者是 socket 被关闭或重
置时(在此情况下, recv 会返回一个空字符串).
•  当非阻塞调用 connect 方法后建立连接或是数据可以被写入到 socket
时, socket 就成为可写的.
•  当非阻塞调用 connect 方法后连接失败后, socket 会发出一个错误信
号.

'''
import select
import socket
import time

PORT = 8037

TIME1970 = 2208988800

service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", PORT))
service.listen(1)
print("listening on port", PORT)

while 1:
	is_readable = [service]
	is_writable = []
	is_error = []
	r, w, e = select.select(is_readable, is_writable, is_error, 1.0)
	if r:
		channel, info = service.accept()
		print("connection from", info)
		t = int(time.time()) + TIME1970
		t = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
		channel.send(t) # send timestamp
		channel.close() # disconnect
	else:
		print("still waiting")


'''
我们等待监听 socket 变成可读状态, 这代表有一个连接
请求到达. 我们用和之前一样的方法处理 channel socket , 因为它不可能因为
等待 4 字节而填充网络缓冲区. 如果你需要向客户端发送大量的数据, 那么你
应该在循环的顶端把数据加入到 is_writable 列表中, 并且只在 select 允许
的情况下写入.
如果你设置 socket 为 非阻塞 模式(通过调用 setblocking 方法), 那么你就
可以使用 select 来等待 socket 连接. 不过 asyncore 模块(参见下一节)提
供了一个强大的框架, 它自动为你处理好了这一切. 所以我不准备在这里多说
什么, 看下一节吧.
'''