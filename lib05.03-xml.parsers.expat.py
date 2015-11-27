'''
xml.parsers.expat 模块

(可选) xml.parsers.expat 模块是 James Clark's Expat XML parser 的接口.
'''
from xml.parsers import expat

class Parser:
	def __init__(self):
		self._parser = expat.ParserCreate()
		self._parser.StartElementHandler = self.start
		self._parser.EndElementHandler = self.end
		self._parser.CharacterDataHandler = self.data
	def feed(self, data):
		self._parser.Parse(data, 0)
	def close(self):
		self._parser.Parse("", 1) # end of data
		del self._parser # get rid of circular references
	def start(self, tag, attrs):
		print("START", repr(tag), attrs)
	def end(self, tag):
		print("END", repr(tag))
	def data(self, data):
		print("DATA", repr(data))

p = Parser()
p.feed("<tag>data</tag>")
p.close()







# 使用 xml.parsers.expat 模块读取 ISO Latin-1 文本
from xml.parsers import expat

class Parser:
	def __init__(self):
		self._parser = expat.ParserCreate()
		self._parser.StartElementHandler = self.start
		self._parser.EndElementHandler = self.end
		self._parser.CharacterDataHandler = self.data
	def feed(self, data):
		self._parser.Parse(data, 0)
	def close(self):
		self._parser.Parse("", 1) # end of data
		del self._parser # get rid of circular references
	def start(self, tag, attrs):
		print("START", repr(tag), attrs)
	def end(self, tag):
		print("END", repr(tag))
	def data(self, data):
		print("DATA", repr(data))

p = Parser()
p.feed("""\
<?xml version='1.0' encoding='iso-8859-1'?>
<author>
<name>fredrik lundh</name>
<city>link?ping</city>
</author>
"""
)
p.close()














