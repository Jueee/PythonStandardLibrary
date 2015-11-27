'''
UserDict 模块

UserDict 模块包含了一个可继承的字典类


'''
# 使用 UserDict 模块
# 下例展示了一个增强的字典类, 允许对字典使用 "加/+" 操作并提供了接受关键字参数的构造函数.
'''
python3中“少”了很多python2的包，在大多情况下这些包之是改了个名字而已。我们可以在import的时候对这些问题进行处理。

try:    #python2
	from UserDict import UserDict
	#建议按照python3的名字进行import
	from UserDict import DictMixin as MutableMapping
except ImportError: 	#python3
	from collections import UserDict
	from collections import MutableMapping
'''
from collections import UserDict

class FancyDict(UserDict):
	def __init__(self, data = {}, **kw):
		UserDict.__init__(self)
		self.update(data)
		self.update(kw)
	def __add__(self,other):
		dict = FancyDict(self.data)
		dict.update(b)
		return dict

a = FancyDict(a = 1)
b = FancyDict(b = 2)
print(a + b)


'''
{'a': 1, 'b': 2}
'''


