'''
tempfile 模块

tempfile 模块允许你快速地创建名称唯一的临时文件供使用.
'''
import tempfile
import os

tempfile = tempfile.mktemp()
print('tempfile','=>',tempfile)

file = open(tempfile, 'w+b')
# TypeError: 'str' does not support the buffer interface
# 新版本的python对字符串对象做了很大的更改，使得原先的函数产生了很大的不同，所以我们需要添加一个参数。
# 由 file.write('*' * 1200) 更变为 file.write(b'*' * 1200)
file.write(b'*' * 1200)
file.seek(0)
print(len(file.read()),'bytes')
file.close()

try:
	# must remove file when done
	os.remove(tempfile)
except OSError:
	pass






# 使用 tempfile 模块打开临时文件
# TemporaryFile 函数会自动挑选合适的文件名, 并打开文件
# 而且它会确保该文件在关闭的时候会被删除.
import tempfile
file = tempfile.TemporaryFile()
for x in range(200):
	file.write(b'*' * 300)
	file.seek(0)  # file.seek(0)是重新定位在文件的第0位及开始位置 
	print(len(file.read()),'bytes')
file.close()      # removes the file !