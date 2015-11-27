'''
rlcompleter 模块

(可选, 只用于 Unix ) rlcompleter 模块为 readline 模块提供了单词自动完成功能.

导入该模块就可以启动自动完成功能. 
默认情况下完成函数被绑定在了 Esc 键上. 
按两次 Esc 键就可以自动完成当前单词. 

你可以使用下面的代码修改所绑定的键:
import readline
readline.parse_and_bind("tab: complete")


1. 该sys.maxint常数已被删除，因为不再有限制 到整数的值。然而，sys.maxsize可以作为 整数比任何实际的列表或字符串索引更大。它符合 “自然”整数大小和通常的 作为sys.maxint在发布平台上（假设 构建选项）。 
2. Python 3的整数没有最大。 如果你的目的是确定在C方式的Python是一个int的最大大小，你的结构模块，找出：
>>> import struct
>>> platform_c_maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
'''
import rlcompleter
import sys
import struct

complete = rlcompleter.Completer()

platform_c_maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1

for phrase in 'co', 'sys.p', 'is':
	print(phrase, '=>', end = '')
	# emulate readline completion handler
	try:
		for index in range(platform_c_maxint):
			term = completer.complete(phrase, index)
			if term is None:
				break
			print(term, end = '')
	except:
		pass
	print()