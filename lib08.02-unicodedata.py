'''
unicodedata 模块

unicodedata 模块包含了 Unicode 字符的属性, 例如字符类别, 分解数据, 以及数值.
'''
import unicodedata

for char in [u'A', u'-', u'1', u'w']:
	print(char,'-> ' ,end = '')
	print(repr(char), '-> ' ,end = '')
	print(unicodedata.category(char), '-> ' ,end = '')
	print(repr(unicodedata.decomposition(char)), '-> ' ,end = '')
	print(unicodedata.decimal(char, None),'=> ', end = '')
	print(unicodedata.numeric(char,None), end = '')
	print()