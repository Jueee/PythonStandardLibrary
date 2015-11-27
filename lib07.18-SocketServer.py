'''
SocketServer 模块

SocketServer 为各种基于 socket 的服务器提供了一个框架. 该模块提供了大
量的类, 你可以用它们来创建不同的服务器.
'''
# 使用 SocketServer 模块
import socketserver
import time

# user-accessible port
PORT = 8037
# reference time
TIME1970 = 2208988800

class TimeRequestHandler(socketserver.StreamRequestHandler):
	def handle(self):
		print("connection from", self.client_address)
		t = int(time.time()) + TIME1970
		b = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
		self.wfile.write(b)

server = socketserver.TCPServer(("", PORT), TimeRequestHandler)
print("listening on port", PORT)
server.serve_forever()