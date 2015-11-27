'''
httplib 模块

httplib 模块提供了一个 HTTP 客户端接口

原来Python 2.x中的"httplib"模块在Python 3.x中变成了"http.client"
'''
'''
import http.client

USER_AGENT = 'lib07.12-httpllib.py'

class Error():
	"""indicates an HTTP error"""
	def __init__(self, irl, errcode, errmsg, headers):
		self.url = url
		self.errcode = errcode
		self.errmsg = errmsg
		self.headers = headers
	def __repr__(self):
		return ('<Error for %s:%s %s>' % (self.url, self.errcode, self.errmsg))

class Server():
	"""docstring for Server"""
	def __init__(self, host):
		self.host = host
	def fetch(self, path):
		http = http.client.HTTP(self.host)
		# write header
		http.putrequest('GET', path)
		http.putheader('User-Agent', USER_AGENT)
		http.putheader('Host', self.host)
		http.putheader('Accept', '*/*')
		http.endheaders()
		# get response
		errcode, errmsg, headers = http.getreply()
		if errcode != 200:
			raise(Error(errcode, errmsg, headers))
		file = http.getfile()
		return file.read()

if __name__ == '__main__':
	server = Server('www.baidu.com')
	print(server.fetch('/index.htm'))
				
'''	


# 使用 httplib 发送数据
import http.client

USER_AGENT = 'lib07.12-httpllib.py'

def post(host, path, data, thpe = None):
	http = http.client.HTTP(host)
	# write header
	http.putrequest("PUT", path)
	http.putheader("User-Agent", USER_AGENT)
	http.putheader("Host", host)
	if type:
		http.putheader("Content-Type", type)
	http.putheader("Content-Length", str(len(size)))
	http.endheaders()
	# write body
	http.send(data)
	# get response
	errcode, errmsg, headers = http.getreply()
	if errcode != 200:
		raise Error(errcode, errmsg, headers)
	file = http.getfile()
	return file.read()

if __name__ == '__main__':
	print(dir(http.client))
	post('www.baidu.com', '/index.htm', 'a piece of data', 'text/plain')















