'''
socket 模块

socket 模块实现了到 socket 通讯层的接口. 你可以使用该模块创建客户端或
是服务器的 socket .
'''
# 使用 socket 模块实现一个时间客户端
# 客户端连接到一个时间协议服务器, 读取 4 字节的返回数据, 并把它转换为一个时间值.
import socket
import struct, time

# server   百度搜索的端口是80
HOST = 'www.baidu.com'
PORT = 80

# reference time (in seconds since 1900-01-01 00:00:00)
TIME1970 = 2208988800

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(s)
'''
# read 4 bytes, and convert to time value
t = s.recv(4)
t = struct.unpack('!I', t)[0]
t = int(t - TIME1970)

s.close()

print('server time is', time.ctime(t))
print('local clock is', int(time.time()) - t, 'seconds off')
'''









'''
socket 工厂函数( factory function )根据给定类型(该例子中为 Internet
stream socket , 即就是 TCP socket )创建一个新的 socket . connect 方法
尝试将这个 socket 连接到指定服务器上. 成功后, 就可以使用 recv 方法读
取数据.

创建一个服务器 socket 使用的是相同的方法, 不过这里不是连接到服务器,
而是将 socket bind (绑定)到本机的一个端口上, 告诉它去监听连接请求, 然
后尽快处理每个到达的请求.
'''

# 使用 socket 模块实现一个时间服务器
# 创建了一个时间服务器, 绑定到本机的 8037 端口( 1024 前的所有端口是为系统服务保留的, Unix 系统下访问它们你必须要有 root 权限).
import socket
import struct, time
# user-accessible port
PORT = 8037
# reference time
TIME1970 = 2208988800
# establish server
service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(('', PORT))
service.listen(1)

print('listening on port', PORT)
'''
while 1:
	# serve forever
	channel, info = service.accept()
	print('connection from', info)
	t = int(time.time()) + TIME1970
	t = struct.pack('!I', t)
	channel.send(t)
	channel.close()
'''

'''
listen 函数的调用告诉 socket 我们期望接受连接. 参数代表连接的队列(用
于在程序没有处理前保持连接)大小. 最后 accept 循环将当前时间返回给每个
连接的客户端.
注意这里的 accept 函数返回一个新的 socket 对象, 这个对象是直接连接到
客户端的. 而原 socket 只是用来保持连接; 所有后来的数据传输操作都使用
新的 socket .
'''











