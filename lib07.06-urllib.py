'''
urllib 模块

urlib 模块为 HTTP , FTP , 以及 gopher 提供了一个统一的客户端接口. 
它会自动地根据 URL 选择合适的协议处理器.

从 URL 获取数据是非常简单的. 
只需要调用 urlopen 方法, 然后从返回的流对象中读取数据即可.

2.x版本的python可以直接使用import urllib来进行操作，但是3.x版本的python使用的是import urllib.request来进行操作.
'''
# 使用 urllib 模块获取远程资源
import urllib.request

fp = urllib.request.urlopen('http://www.baidu.com')
op = open('samples/out.html','wb')

n = 0
while 1:
	s = fp.read(8192)
	if not s:
		break
	op.write(s)
	n = n + len(s)

fp.close()
op.close()
# 这个流对象提供了一些非标准的属性.
# headers 是一个  Message 对象(在 mimetools 模块中定义), url 是实际的 URL . 后者会根据服务器的重定向而更新.

for k, v in fp.headers.items():
	print(k, '=', v)
print('copied', n, 'bytes from', fp.url)








# 用 urllib 模块实现自动身份验证
# urlopen 函数实际上是一个辅助函数, 它会创建一个  FancyURLopener 类的实例并调用它的 open 方法.
# 可以继承这个类来完成特殊的行为.
import urllib.request

class myURLOpener(urllib.request.FancyURLopener):
	"""read an URL, with automatic HTTP authentication"""
	def setpasswd(self, user, passwd):
		self.__user = user
		self.__passwd = passwd
	def prompt_user_passwd(self, host, realm):
		return self.__user, self.__passwd

urlopener = myURLOpener()
urlopener.setpasswd('mulder', 'trustnol')

fp = urlopener.open('http://www.baidu.com')
print(fp.read())
