'''
zlib 模块

zlib 模块为 "zlib" 压缩提供支持. (这种压缩方法是 "deflate".)
'''

# 使用 zlib 模块压缩字符串
# 使用 compress 和 decompress 函数接受字符串参数.
import zlib

MESSAGE = b'life of brian'

compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)

print('original:', MESSAGE)
print('compressed_message', compressed_message)
print('decompressed_message', decompressed_message)






# 使用 zlib 模块压缩多个不同类型文件
# 文件的内容决定了压缩比率
import zlib
import glob

for file in glob.glob('samples/*'):
	indata = open(file, 'rb').read()
	outdata = zlib.compress(indata,zlib.Z_BEST_COMPRESSION)

	print(file, len(indata), '=>', len(outdata),'', end = '')
	print('%d%%' % (len(outdata) * 100 / len(indata)))


print('----------------')


# 使用 zlib 模块解压缩流
# 可以实时地压缩或解压缩数据
import zlib

encoder = zlib.compressobj()

data = encoder.compress(b'life')
data = data + encoder.compress(b'of')
data = data + encoder.compress(b'brian')
data = data + encoder.flush()

print(data)
print(zlib.decompress(data))


print('----------------')



# 压缩流的仿文件访问方式
# 把解码对象封装到了一个类似文件对象的类中, 实现了一些文件对象的方法, 这样使得读取压缩文件更方便.
import zlib
import io

class ZipInputStream(object):
	"""docstring for ZipInputStream"""
	def __init__(self, file):
		self.file = file
		self.__rewind()
	def __rewind(self):
		self.zip = zlib.decompressobj()
		self.pos = 0    # position in zipped stream
		self.offset = 0 # position in unzipped stream
		self.data = ''
	def __fill(self, bytes):
		if self.zip:
			# read until we have enough bytes in the buffer
			while not bytes or len(self.data) < bytes:
				self.file.seek(self.pos)
				data = self.file.read(16384)
				if not data:
					self.data = self.data + self.zip.flush()
					self.zip = None
					break
				self.pos = self.pos + len(data)
				self.data = self.data + self.zip.decompress(data)
	def seek(self, offset, whence = 0):
		if whence == 0:
			position = offset
		elif whence ==1:
			position = self.offset + offset
		else:
			raise(IOError, 'Illegal argument')
		if position < self.offset:
			raise(IOError, 'Cannot seek backwards')

		while position > self.offset:
			if not self.read(min(position - self.offset, 16384)):
				break
	def tell(self):
		return self.offset
	def read(self, bytes = 0):
		self.__fill(bytes)
		if bytes:
			data = self.data[:bytes]
			self.data = self.data[bytes:]
		else:
			data = self.data
			self.data = ''
		self.offset = self.offset + len(data)
		return data
	def readline(self):
		while self.zip and '\n' not in self.data:
			self.__fill(len(self.data) + 512)
		i = str.find(self.data, '\n') + 1
		if i <= 0:
			return self.read()
		return self.read(i)
	def readlines(self):
		lines = []
		while 1:
			s = self.readline()
			if not s:
				break
			lines.append(s)
		return lines

data = open('samples/sample.txt').read()
print(data)
bdata = data.encode(encoding='gb2312')
bdata = zlib.compress(bdata)
print(bdata)

file = ZipInputStream(io.StringIO(data))		
for line in file.readlines():
	print(line[:-1])
