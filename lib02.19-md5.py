'''
md5 模块

md5 (Message-Digest Algorithm 5)模块用于计算信息密文(信息摘要).

md5 算法计算一个强壮的 128 位密文. 
这意味着如果两个字符串是不同的, 那么有极高可能它们的 md5 也不同. 
也就是说, 给定一个 md5 密文, 那么几乎没有可能再找到另个字符串的密文与此相同.

python3.x已经把md5 module移除了。
要想用md5得用 hashlib module


【注】内建的伪随机生成器对于加密操作而言并不合适.
'''

# 使用 md5 模块
from hashlib import md5

hash = md5()
# #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误  
hash.update(b'spam, spam, and eggs')
print(repr(hash.hexdigest()))
print(repr(hash.digest()))		# 校验和是一个二进制字符串




# 使用 md5 模块获得十六进制或 base64 编码的 md5 值

from hashlib import md5
import base64

hash = md5()
hash.update(b'spam, spam, and eggs')

value = hash.digest()
print(hash.hexdigest())
print(base64.encodestring(value))





# 使用 md5 模块来处理口令的发送与应答的验证
from hashlib import md5
import random

def getchallenge():
	# 生成一个 16 字节长的随机字符串. 注意内建的伪随机生成器
	# 使用的是 24 位的种子(seed), 所以这里这样用并不好..
	challenge = map(lambda i : chr(random.randint(0, 255)), range(16))
	print(challenge)
	return ''.join(challenge)

def getresponse(password, challenge):
	# 计算密码和质询(challenge)的联合密文
	m = md5()
	# #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
	m.update(password.encode(encoding='gb2312'))
	m.update(challenge)
	return m.digest()

# 服务器/客户端通讯
# 1. 客户端连接, 服务器发布质询(challenge)
print('client:', 'connect')
challenge = getchallenge()
print('server:', challenge.encode('utf-8'))

# 2. 客户端计算密码和质询(challenge)的组合后的密文
client_response = getresponse('trustno1', challenge.encode('utf-8'))
print('client:', client_response)

# 3. 服务器做同样的事, 然后比较结果与客户端的返回,
# 判断是否允许用户登陆. 这样做密码没有在通讯中明文传输.
server_response = getresponse('trustno1' ,challenge.encode('utf-8'))
if server_response == client_response:
	print('server:', 'login ok') 






# 使用 md5 模块检查数据完整性
# 可以通过标记信息来判断它是否在网络传输过程中被修改(丢失).
from hashlib import md5
import array

class HMAC_MD5():
	"""keyed md5 message authentication"""
	def __init__(self, key):
		if len(key) > 64:
			key = md5(key).digest()
		ipad = array.array('B', [0x36] * 64)
		opad = array.array('B', [0x5C] * 64)
		for i in range(len(key)):
			ipad[i] = ipad[i]^ord(key[i])
			opad[i] = opad[i]^ord(key[i])
		self.ipad = md5(ipad.tostring())
		self.opad = md5(opad.tostring())

	def digest(self, data):
		# copy 方法会对这个内部对象状态做一个快照( snapshot ). 
		# 这允许你预先计算部分密文摘要
		ipad = self.ipad.copy()
		opad = self.opad.copy()
		ipad.update(data.encode(encoding='gb2312'))
		opad.update(ipad.digest())

# 模拟服务器端
key = 'this should be a well-kept secret'
message = open('samples/sample.txt').read()

signature = HMAC_MD5(key).digest(message)

# (经过由网络发送信息和签名)

# 模拟客户端
key = 'this should be a well-kept secret'
client_response = HMAC_MD5(key).digest(message)
if client_response == signature:
	print('this is the original message')
	print('')
	print(message)
else:
	print('someone has modified the message!!!')