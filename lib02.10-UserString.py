'''
UserString 模块

UserString 模块包含两个类,  UserString 和  MutableString . 前
者是对标准字符串类型的封装, 后者是一个变种, 允许你修改特定位置的字符
(联想下列表就知道了).


关于UserString类

对于2.X版本：Python文档中提到，如果不涉及到2.2以前的版本，请考虑直接使用str类型来代替UserString类型。

对于3.X版本：该模块已经移到collection模块中。 
'''
from collections import UserString

class myString(UserString):
	"""docstring for myString"""
	def append(self, s):
		self.data = self.data + s
	def insert(self,index,s):
		self.data = self.data[index:] + s + self.data[index:]
	def remove(self,s):
		self.data = self.data.replace(s,'')

file = open('samples/book.txt')
text = file.read()
file.close()

book = myString(text)
for bird in ['gannet','robin','nuthatch']:
	book.remove(bird)

print(book)