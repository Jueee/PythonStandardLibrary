'''
cStringIO 模块

cStringIO 是一个可选的模块, 是 StringIO 的更快速实现. 
它的工作方式和 StringIO 基本相同, 但是它不可以被继承. 

Python3 移除了StringIO和cStringIO。
加入了io模块,并分别使用io.StringIO和io.BytesIO分别用于text和data。
'''

import io
MESSAGE = 'That man is depriving a village somewhere of a computer scientist.'
help(io.BytesIO)
file = io.StringIO(MESSAGE)

print(file.read())


# 为了让你的代码尽可能快, 但同时保证兼容低版本的 Python ,你可以使用一个小技巧在 cStringIO 不可用时启用 StringIO 模块
import io
try:
	StringIO = io.BytesIO
except ImportError:
	StringIO = io.StringIO

print(StringIO)

