'''
gzip 模块

gzip 模块用来读写 gzip 格式的压缩文件
'''

# 使用 gzip 模块读取压缩文件
import gzip

file = gzip.GzipFile('samples/sample.gz')

print(file.read())







# 给 gzip 模块添加 seek/tell 支持
import gzip

class gzipFile(gzip.GzipFile):
	"""adds seek/tell support to GzipFile"""
	
	offset = 0

	def read(self, size = 1000):
		data = gzip.GzipFile.read(self, size)
		self.offset = self.offset + len(data)
		return data

	def seek(self, offset, whence = 0):
		# figure out new position (we can only seek forwards)
		if whence == 0:
			position = offset
		elif whence == 1:
			position = self.offset + offset
		else:
			raise(IOError, 'Illeagal argument')
		if position < self.offset:
			raise(IOError, 'Connot seek backwards')

		while position > self.offset:
			if not self.read(min(position - self.offset, 16384)):
				break
	def tell(self):
		return self.offset


file = gzipFile('samples/sample.gz')
file.seek(80)
print(file.read())



