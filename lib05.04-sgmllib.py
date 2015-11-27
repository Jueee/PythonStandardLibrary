'''
sgmllib 模块

sgmllib 模块, 提供了一个基本的 SGML 语法分析器. 
它与 xmllib 分析器基本相同, 但限制更少(而且不是很完善). 

和在 xmllib 中一样, 这个分析器在遇到起始标签, 数据区域, 结束标签以及实体时调用内部方法. 

sgmllib是2.6以后引入python,在3.0以后这个库被移除了。
'''

# 使用 sgmllib 模块提取 Title 元素
import sgmllib

class FoundTitle(Exception):
	pass
class ExtractTitle(sgmllib.SGMLParser):
	def __init__(self, verbose=0):
		sgmllib.SGMLParser.__init__(self, verbose)
		self.title = self.data = None
	def handle_data(self, data):
		if self.data is not None:
			self.data.append(data)
	def start_title(self, attrs):
		self.data = []
	def end_title(self):
		self.title = string.join(self.data, "")
		raise FoundTitle # abort parsing!
def extract(file):
	# extract title from an HTML/SGML stream
	p = ExtractTitle()
	try:
		while 1:
			# read small chunks
			s = file.read(512)
			if not s:
				break
			p.feed(s)
		p.close()
	except FoundTitle:
		return p.title
	return None
#
# try it out
print("html", "=>", extract(open("samples/sample.htm")))
print("sgml", "=>", extract(open("samples/sample.sgm")))