'''
StringIO 模块

StringIO 模块实现了一个工作在内存的文件对象 (内存文件). 
在大多需要标准文件对象的地方都可以使用它来替换.

Python3 移除了StringIO和cStringIO。
加入了io模块,并分别使用io.StringIO和io.BytesIO分别用于text和data。
'''

# 使用 StringIO 模块从内存文件读入内容
#from io import StringIO as StringIO
import io
MESSAGE = 'That man is depriving a village somewhere of a commputer scientist.'
file = io.StringIO(MESSAGE)
print(file.read())


# 使用 StringIO 模块向内存文件写入内容
import io
file = io.StringIO()
file.write('This man is no ordinary man.')
file.write('This is Mr.F.G.Superman.')

print(file.getvalue())





# 使用 StringIO 模块捕获输出
# StringIO 可以用于重新定向 Python 解释器的输出
import io
import sys

stdout = sys.stdout
sys.stdout = file = io.StringIO()
print("""
According to Gbaya folktales, trickery and guile
are the best ways to defeat the python, king of
snakes, which was hatched from a dragon at the
world's start. -- National Geographic, May 1997
	""")

sys.stdout = stdout
print(str.upper(file.getvalue()))