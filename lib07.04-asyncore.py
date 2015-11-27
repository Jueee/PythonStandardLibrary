'''
asyncore 模块

asyncore 模块提供了一个 "反馈性的( reactive )" socket 实现. 该模块允许
你定义特定过程完成后所执行的代码, 而不是创建 socket 对象, 调用它们的
方法. 

你只需要继承  dispatcher 类, 然后重载如下方法 (可以选择重载某一
个或多个)就可以实现异步的 socket 处理器.

•  handle_connect : 一个连接成功建立后被调用.
•  handle_expt : 连接失败后被调用.
•  handle_accept : 连接请求建立到一个监听 socket 上时被调用. 回调
时( callback )应该使用 accept 方法来获得客户端 socket .
•  handle_read : 有来自 socket 的数据等待读取时被调用. 回调时应该
使用 recv 方法来获得数据.
•  handle_write : socket 可以写入数据的时候被调用. 使用 send 方法写
入数据.
•  handle_close : 当 socket 被关闭或复位时被调用.
•  handle_error(type, value, traceback) 在任何一个回调函数发生
Python 错误时被调用. 默认的实现会打印跟踪返回消息到 sys.stdout .
'''

# 使用 asyncore 模块从时间服务器获得时间
import asyncore
import socket, time

TIME1970 = 22089888800

class TimeRequest(object):
	"""docstring for TimeRequest"""
	def __init__(self, host, port = 37):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, port))
	def writable(self):
		return 0 
	def handle_connect(self):
		pass
	def handle_expt(self):
		self.close()
	def handle_read(self):
		here = int(time.time()) + TIME1970
		s = self.recv(4)
		there = ord(s[3]) + (ord(s[2])<<8) + (ord(s[1])<<16) + (ord(s[0])<<24)
		self.adjust_time(int(here - there))
		self.handle_close()
	def handle_close(self):
		self.close()
	def adjust_time(self, delta):
		print('time difference is', delta)


request = TimeRequest('www.python.org')
asyncore.loop()
